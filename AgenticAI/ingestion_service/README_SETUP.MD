# Envirnoment setup (Python 3.11.9)
-- python -m venv genai_api_env
## Overrride the python version with 3.11 
-- py -3.11 -m venv genai_api_env
## Activate Env
-- genai_api_env\Scripts\activate

### Exe requirements.txt for lib setup 
-- pip install -r requirements.txt

# Application 
## Run -- uvicorn app.main:app --reload --port 8002

# Deletion 
-- rmdir /s /q genai_api_env
