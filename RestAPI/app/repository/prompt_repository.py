from app.repository.db_connection import get_db_connection


def insert_user_prompt_log(
    user_name: str,
    question: str,
    response: str,
    model_used: str,
    provider: str,
    department: str,
    tokens_used: int = None,
):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        EXEC sp_InsertUserPromptLog
            @UserName = ?,
            @ProviderName = ?,
            @ModelName = ?,
            @Question = ?,
            @Response = ?,
            @TokensUsed = ?,
            @Department = ?
        """,
        user_name,
        provider,
        model_used,
        question,
        response,
        tokens_used,
        department,
    )

    conn.commit()
    cursor.close()
    conn.close()
