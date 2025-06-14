# app.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import base64
import tempfile
import uvicorn
from utils import generate_answer

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: str = None
def fix_base64_padding(b64_string):
    return b64_string + '=' * (-len(b64_string) % 4)

@app.post("/api/")
async def answer_question(data: QuestionRequest):
    image_path = None
    if data.image:
        try:
            decoded_image = base64.b64decode(fix_base64_padding(data.image))
            with tempfile.NamedTemporaryFile(delete=False, suffix=".webp") as f:
                f.write(decoded_image)
                image_path = f.name
        except Exception as e:
            return {"error": f"Image decode failed: {str(e)}"}

    answer, links = generate_answer(data.question, image_path)
    return {"answer": answer, "links": links}
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
