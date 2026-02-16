from app.repository.db_connection import get_db_connection


class LogRepository:

    @staticmethod
    def log_prompt(user_id, prompt, department, model_used, provider):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            EXEC sp_InsertUserPromptLog
                @UserId=?,
                @Prompt=?,
                @Department=?,
                @ModelUsed=?,
                @Provider=?
            """,
            user_id,
            prompt,
            department,
            model_used,
            provider
        )

        conn.commit()
        conn.close()

    @staticmethod
    def log_error(user_id, error_type, error_message, stack_trace):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            EXEC sp_InsertErrorLog
                @UserId=?,
                @ErrorType=?,
                @ErrorMessage=?,
                @StackTrace=?
            """,
            user_id,
            error_type,
            error_message,
            stack_trace
        )

        conn.commit()
        conn.close()
