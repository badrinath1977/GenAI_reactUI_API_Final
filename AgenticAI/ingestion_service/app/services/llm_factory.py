from langchain_openai import ChatOpenAI

# 🔴 TEMPORARY HARDCODE FOR TESTING
OPENAI_KEY = "Put your OpenAI key here"


_llm_instance = None


def get_llm():
    global _llm_instance

    if _llm_instance is None:
        _llm_instance = ChatOpenAI(
            model="gpt-3.5-turbo",
            openai_api_key=OPENAI_KEY,
            temperature=0
        )

    return _llm_instance
