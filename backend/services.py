import asyncio
import openai
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAIService:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o")
        self.prompt = "You are taciturn detective in a noir movie. Respond as such."

    async def get_answer_openai(self, query: str)->dict:
        try:
            async with asyncio.timeout(15):
                response = await self.client.responses.create(
                    model=self.model,
                    instructions=self.prompt,
                    input=query
                )
                

                extracted_response = self.extract_response_text(response)

                return extracted_response
                
        except openai.APIConnectionError:
            raise openai.APIConnectionError
        except openai.AuthenticationError:
            raise openai.AuthenticationError

    def extract_response_text(self, response) -> str:
        text = getattr(response, "output_text", None)
        if text:
            return text.strip()
        parts = []
        out_list = None
        if isinstance(response, dict):
            out_list = response.get("output", []) or []
        else:
            out_list = getattr(response, "output", []) or []

        for item in out_list:
            if isinstance(item, dict):
                content = item.get("content", []) or []
            else:
                content = getattr(item, "content", []) or []

            for c in content:
                # c may be dict {"type":"output_text","text":"..."}
                if isinstance(c, dict):
                    # prefer text when type is output_text, but accept any text field
                    t = c.get("text")
                    if t:
                        parts.append(t)
                else:
                    t = getattr(c, "text", None)
                    if t:
                        parts.append(t)

        return "\n".join(p.strip() for p in parts if p).strip()

    # async def get_answer_stubbed(query: str) -> dict:
    #     await asyncio.sleep(2)
    #     response = f"This is a stubbed answer for the query: '{query}'. Normally, this would come from OpenAI's chat model."
    #     return {"answer" : response}