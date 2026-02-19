from fastapi import FastAPI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config.settings import settings
from app.core.database import get_llm_provider, log_prompt, log_error

app = FastAPI()

@app.get("/ask")
def ask(query: str, username: str = "system"):
    try:
        provider = get_llm_provider(settings.OPENAI_PROVIDER_NAME)

        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=provider.ApiKeyEncrypted
        )

        db = FAISS.load_local(settings.VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
        docs = db.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])

        llm = ChatOpenAI(
            model=provider.ModelName,
            api_key=provider.ApiKeyEncrypted
        )

        prompt = f"Context:\n{context}\n\nQuestion:{query}"
        response = llm.invoke(prompt)

        log_prompt(username, provider.ProviderName, provider.ModelName, query, response.content, None, None)

        return {"answer": response.content}

    except Exception as e:
        log_error(username, "ChatError", str(e), "")
        return {"error": str(e)}
