from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryInput(BaseModel):
    query: str

@app.post("/api/answer")
async def get_answer(input: QueryInput):
    query = input.query

    # Validate query: non-empty, max 2000 chars
    if not query or not isinstance(query, str):
        raise HTTPException(status_code=400, detail="Query is required and must be a string")
    if len(query) > 2000:
        raise HTTPException(status_code=400, detail="Query exceeds 2000 character limit")

    # Stubbed OpenAI response (since no API key)
    try:
        # Simulate API delay for realism
        await asyncio.sleep(1)
        stubbed_response = f"This is a stubbed answer for the query: '{query}'. Normally, this would come from OpenAI's chat model."
        return {"answer": stubbed_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to process query")

# Run with: uvicorn main:app --host 0.0.0.0 --port 8000