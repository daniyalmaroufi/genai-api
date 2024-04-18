from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

import os
GOOGLE_GENAI_API_KEY = os.environ.get("GOOGLE_GENAI_API_KEY")

genai.configure(api_key=GOOGLE_GENAI_API_KEY)

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate/")
def generate(prompt: Prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt.text)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

