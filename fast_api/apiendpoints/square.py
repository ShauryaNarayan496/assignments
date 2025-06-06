from fastapi import FastAPI

app = FastAPI()

@app.get("/square/{number}")
def square(number: int):
    return {"square": number * number}