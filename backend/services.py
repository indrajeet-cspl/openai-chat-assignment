import asyncio


        
async def get_answer_stubbed(query: str) -> dict:
    await asyncio.sleep(2)
    response = f"This is a stubbed answer for the query: '{query}'. Normally, this would come from OpenAI's chat model."
    return {"answer" : response}