from app.repository.db_connection import get_db_connection


# ---------------------------------------------------------
# Insert File Metadata
# ---------------------------------------------------------
def insert_file_metadata(
    file_name: str,
    original_file_name: str,
    file_size: int,
    content_type: str,
    file_extension: str,
    file_path: str,
    department: str,
    user_id: str,
    fingerprint: str
):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        EXEC sp_InsertFileMetadata
            @FileName=?,
            @OriginalFileName=?,
            @FileSize=?,
            @ContentType=?,
            @FileExtension=?,
            @FilePath=?,
            @Department=?,
            @UserId=?,
            @FingerPrint=?
        """,
        file_name,
        original_file_name,
        file_size,
        content_type,
        file_extension,
        file_path,
        department,
        user_id,
        fingerprint
    )

    conn.commit()
    cursor.close()
    conn.close()


# ---------------------------------------------------------
# Check Duplicate Fingerprint
# ---------------------------------------------------------
def get_file_by_fingerprint(fingerprint: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT TOP 1 Id
        FROM FileMetadata
        WHERE FingerPrint = ?
        """,
        fingerprint
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
