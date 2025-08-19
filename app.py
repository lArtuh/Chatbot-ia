from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI


client = OpenAI(api_key="YOUR_API_KEY_HERE")


app = FastAPI(title="API chatbot with OpenAI")


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # you can switch to gpt 5
            messages=[
                {"role": "system",
                    "content": "You are an assistant at company x in charge of customer service."},
                {"role": "user", "content": request.message}
            ]
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
