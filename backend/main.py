import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from pathlib import Path

# load_dotenv(Path(__file__).resolve().parent / ".env")
from schemas import QueryInput
from services import OpenAIService
load_dotenv()

app = FastAPI()
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"{frontend_url}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai_service = OpenAIService()

@app.post("/api/answer")
async def get_answer(input: QueryInput):
    query = input.query
    # Validate query: non-empty, max 2000 chars
    if not query or not isinstance(query, str):
        raise HTTPException(status_code=400, detail="Query is required and must be a string")
    if len(query) > 2000:
        raise HTTPException(status_code=400, detail="Query exceeds 2000 character limit")
    
    try:
        response = await openai_service.get_answer_openai(query=query)
        return {"answer" : response}
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request to OpenAI Service timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error {e}")
