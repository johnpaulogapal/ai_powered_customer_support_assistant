from fastapi import FastAPI
from chat.router import chat_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(chat_router)