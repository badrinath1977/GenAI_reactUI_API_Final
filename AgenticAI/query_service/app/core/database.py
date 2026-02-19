from sqlalchemy import create_engine, text
from app.config.settings import settings

connection_string = (
    f"mssql+pyodbc://@{settings.DB_SERVER}/{settings.DB_DATABASE}?"
    f"driver={settings.DB_DRIVER.replace(' ', '+')}&trusted_connection={settings.DB_TRUSTED_CONNECTION}"
)

engine = create_engine(connection_string)

def get_llm_provider(provider_name):
    with engine.connect() as conn:
        result = conn.execute(
            text("EXEC ApplicationChatbot.sp_GetLLMProvider :provider"),
            {"provider": provider_name}
        ).fetchone()
        return result

def get_embedding_provider(provider_name):
    with engine.connect() as conn:
        result = conn.execute(
            text("EXEC ApplicationChatbot.sp_GetEmbeddingProvider :provider"),
            {"provider": provider_name}
        ).fetchone()
        return result

def log_error(user_id, error_type, message, stack):
    with engine.connect() as conn:
        conn.execute(text(
            "EXEC ApplicationChatbot.sp_InsertErrorLog :user_id, :error_type, :message, :stack"
        ), {
            "user_id": user_id,
            "error_type": error_type,
            "message": message,
            "stack": stack
        })
        conn.commit()

def log_prompt(username, provider, model, question, response, tokens, department):
    with engine.connect() as conn:
        conn.execute(text(
            "EXEC ApplicationChatbot.sp_InsertPromptLog :username, :provider, :model, :question, :response, :tokens, :department"
        ), {
            "username": username,
            "provider": provider,
            "model": model,
            "question": question,
            "response": response,
            "tokens": tokens,
            "department": department
        })
        conn.commit()
