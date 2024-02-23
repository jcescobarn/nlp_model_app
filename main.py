from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get()
def process_text():
    return {"message": "hola"} 


def save_comment():
    return {"message": "saved"}