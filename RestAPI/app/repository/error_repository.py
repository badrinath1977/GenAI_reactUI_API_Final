from app.repository.db_connection import get_db_connection


def insert_error_log(user_id: str, error_type: str, error_message: str, stack_trace: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        EXEC sp_InsertErrorLog 
            @UserId = ?, 
            @ErrorType = ?, 
            @ErrorMessage = ?, 
            @StackTrace = ?
        """,
        user_id,
        error_type,
        error_message,
        stack_trace,
    )

    conn.commit()
    cursor.close()
    conn.close()
