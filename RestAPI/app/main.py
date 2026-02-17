# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.chat_routes import router as chat_router
# from app.api.upload_routes import router as upload_router
# from app.api.health_routes import router as health_router

# app = FastAPI(title="GenAI Enterprise API")

# # CORS Configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # For testing only
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(chat_router, prefix="/chat", tags=["Chat"])
# app.include_router(upload_router, prefix="/upload", tags=["Upload"])
# app.include_router(health_router, prefix="/health", tags=["Health"])

# @app.get("/")
# def root():
#     return {"message": "GenAI Enterprise Backend Running"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat_routes import router as chat_router
from app.api.upload_routes import router as upload_router
from app.api.health_routes import router as health_router

from app.core.logger import logger

# ---------------------------------------
# Create FastAPI App
# ---------------------------------------

app = FastAPI(
    title="GenAI Enterprise API",
    version="1.0.0"
)

# ---------------------------------------
# CORS CONFIGURATION (IMPORTANT)
# ---------------------------------------

app.add_middleware(
    CORSMiddleware,
    # allow_origins=[
    #     "http://localhost:5173",
    #     "http://127.0.0.1:5173",
    # ],
    allow_origins=["*"],  # For testing only, restrict in production

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------
# Include Routers
# ---------------------------------------

app.include_router(chat_router, prefix="/chat")
app.include_router(upload_router, prefix="/upload")
app.include_router(health_router, prefix="/health")

# ---------------------------------------
# Root Endpoint
# ---------------------------------------

@app.get("/")
def root():
    return {"message": "GenAI Enterprise API is running"}

logger.info("Application started successfully")
