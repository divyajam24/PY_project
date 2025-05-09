from fastapi import FastAPI
from pydantic import BaseModel
import asyncio 
app = FastAPI()
class ExplanationRequest(BaseModel):
    concept: str
    audience: str
class ExplanationResponse(BaseModel):
    concept: str
    audience: str
    explanation: str
async def get_mock_explanation(concept: str, audience: str) -> str:
    await asyncio.sleep(1)  
    return f"Okay, imagine explaining '{concept}' to a '{audience}'. It's basically a simplified version of a complex topic meant for easier understanding."
@app.post("/explain", response_model=ExplanationResponse)
async def explain_concept(req: ExplanationRequest):
    explanation_text = await get_mock_explanation(req.concept, req.audience)
    return ExplanationResponse(
        concept=req.concept,
        audience=req.audience,
        explanation=explanation_text
    )
@app.get("/health")
def health_check():
    return {"status":"ok"}
