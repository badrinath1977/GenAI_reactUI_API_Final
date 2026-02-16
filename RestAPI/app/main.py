from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat_routes import router as chat_router
from app.api.upload_routes import router as upload_router
from app.api.health_routes import router as health_router

app = FastAPI(title="GenAI Enterprise API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(upload_router, prefix="/upload", tags=["Upload"])
app.include_router(health_router, prefix="/health", tags=["Health"])

@app.get("/")
def root():
    return {"message": "GenAI Enterprise Backend Running"}
