import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from schemas import QueryInput
from services import get_answer_stubbed
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


@app.post("/api/answer")
async def get_answer(input: QueryInput):
    query = input.query

    # Validate query: non-empty, max 2000 chars
    if not query or not isinstance(query, str):
        raise HTTPException(status_code=400, detail="Query is required and must be a string")
    if len(query) > 2000:
        raise HTTPException(status_code=400, detail="Query exceeds 2000 character limit")

    try:
        async with asyncio.timeout(15):
            response = await get_answer_stubbed(query=query)
            return response
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request to OpenAI Service timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to process query")
