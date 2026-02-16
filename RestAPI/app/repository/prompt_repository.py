from app.repository.db_connection import get_db_connection


def insert_user_prompt_log(user_id: str, prompt: str, model_used: str, provider: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        EXEC sp_InsertUserPromptLog 
            @UserId = ?, 
            @Prompt = ?, 
            @ModelUsed = ?, 
            @Provider = ?
        """,
        user_id,
        prompt,
        model_used,
        provider,
    )

    conn.commit()
    cursor.close()
    conn.close()
