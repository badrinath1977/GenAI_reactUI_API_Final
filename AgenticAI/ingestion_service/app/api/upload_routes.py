# import os
# import shutil
# import hashlib
# import traceback
# from datetime import datetime

# from fastapi import APIRouter, UploadFile, File, Form, Header, HTTPException

# from app.core.config import settings
# from app.core.security import validate_jwt_token
# from app.core.logger import logger

# from app.ingestion.document_ingestor import DocumentIngestor
# from app.services.vector_store_service import VectorStoreService
# from app.repository.file_repository import insert_file_metadata
# from app.repository.error_repository import insert_error_log


# router = APIRouter(prefix="/upload", tags=["Upload"])


# # ---------------------------------------------------------
# # Helper: Generate SHA256 Fingerprint
# # ---------------------------------------------------------

# def generate_fingerprint(file_path: str) -> str:
#     sha256 = hashlib.sha256()
#     with open(file_path, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             sha256.update(chunk)
#     return sha256.hexdigest()


# # ---------------------------------------------------------
# # Upload Document API
# # ---------------------------------------------------------
# # import pdb;pdb.set_trace()

# @router.post("/document")
# async def upload_document(
#     department: str = Form(...),
#     file: UploadFile = File(...),
#     # authorization: str = Header(...)
# ):
#     """
#     Upload document with:
#     - JWT validation
#     - Department isolation
#     - Vector creation per department
#     - Metadata DB storage
#     - Fingerprint generation
#     """

#     try:
#         # ---------------------------------
#         # 1️⃣ Validate JWT
#         # ---------------------------------
#         # validate_jwt_token(authorization)

#         # ---------------------------------
#         # 2️⃣ Create department folder
#         # ---------------------------------
#         department_folder = os.path.join("uploaded_files", department)
#         os.makedirs(department_folder, exist_ok=True)

#         file_path = os.path.join(department_folder, file.filename)

#         # Save file
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         logger.info(f"File uploaded: {file.filename} | Dept: {department}")

#         # ---------------------------------
#         # 3️⃣ Generate Fingerprint
#         # ---------------------------------
#         fingerprint = generate_fingerprint(file_path)

#         # ---------------------------------
#         # 4️⃣ Ingest Document
#         # ---------------------------------
#         ingestor = DocumentIngestor()
#         docs = ingestor.ingest(file_path)

#         # ---------------------------------
#         # 5️⃣ Store into Vector DB (Department-based)
#         # ---------------------------------
#         vector_service = VectorStoreService(department=department)
#         vector_service.add_documents(docs)

#         # ---------------------------------
#         # 6️⃣ Store Metadata in DB
#         # ---------------------------------
#         insert_file_metadata(
#             file_name=file.filename,
#             original_file_name=file.filename,
#             file_size=os.path.getsize(file_path),
#             content_type=file.content_type,
#             file_extension=os.path.splitext(file.filename)[1],
#             file_path=file_path,
#             department=department,
#             user_id="Test_APP",  # Extract from JWT in real implementation
#             fingerprint=fingerprint
#         )

#         return {
#             "message": "File uploaded successfully",
#             "department": department,
#             "fingerprint": fingerprint
#         }

#     except Exception as ex:

#         logger.error(f"Upload Error: {str(ex)}")

#         insert_error_log(
#             user_id=None,
#             error_type="UploadError",
#             error_message=str(ex),
#             stack_trace=traceback.format_exc()
#         )

#         raise HTTPException(status_code=500, detail="File upload failed")


import os
import shutil
import hashlib
import traceback

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.core.logger import logger
from app.ingestion.document_ingestor import DocumentIngestor
from app.services.vector_store_service import VectorStoreService
from app.repository.file_repository import (
    insert_file_metadata,
    get_file_by_fingerprint
)
from app.repository.error_repository import insert_error_log


router = APIRouter(prefix="/upload", tags=["Upload"])


# ---------------------------------------------------------
# Helper: Generate SHA256 Fingerprint
# ---------------------------------------------------------
def generate_fingerprint(file_path: str) -> str:
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


# ---------------------------------------------------------
# Upload Document API
# ---------------------------------------------------------
@router.post("/document")
async def upload_document(
    department: str = Form(...),
    file: UploadFile = File(...)
):
    try:

        # ---------------------------------
        # 1️⃣ Create department folder
        # ---------------------------------
        department_folder = os.path.join("uploaded_files", department)
        os.makedirs(department_folder, exist_ok=True)

        file_path = os.path.join(department_folder, file.filename)

        # ---------------------------------
        # 2️⃣ Save File
        # ---------------------------------
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"File uploaded: {file.filename} | Dept: {department}")

        # ---------------------------------
        # 3️⃣ Generate Fingerprint
        # ---------------------------------
        fingerprint = generate_fingerprint(file_path)

        # ---------------------------------
        # 4️⃣ Check Duplicate
        # ---------------------------------
        existing_file = get_file_by_fingerprint(fingerprint)

        if existing_file:
            os.remove(file_path)  # delete duplicate file

            raise HTTPException(
                status_code=400,
                detail="Duplicate file detected. This file was already uploaded."
            )

        # ---------------------------------
        # 5️⃣ Ingest Document
        # ---------------------------------
        ingestor = DocumentIngestor()
        docs = ingestor.ingest(file_path)

        # ---------------------------------
        # 6️⃣ Store into Vector DB
        # ---------------------------------
        vector_service = VectorStoreService(department=department)
        vector_service.add_documents(docs)

        # ---------------------------------
        # 7️⃣ Store Metadata in DB
        # ---------------------------------
        insert_file_metadata(
            file_name=file.filename,
            original_file_name=file.filename,
            file_size=os.path.getsize(file_path),
            content_type=file.content_type,
            file_extension=os.path.splitext(file.filename)[1],
            file_path=file_path,
            department=department,
            user_id="Test_APP",
            fingerprint=fingerprint
        )

        return {
            "message": "File uploaded successfully",
            "department": department,
            "fingerprint": fingerprint
        }

    except HTTPException:
        raise

    except Exception as ex:

        logger.error(f"Upload Error: {str(ex)}")

        insert_error_log(
            user_id=None,
            error_type="UploadError",
            error_message=str(ex),
            stack_trace=traceback.format_exc()
        )

        raise HTTPException(status_code=500, detail="File upload failed")
