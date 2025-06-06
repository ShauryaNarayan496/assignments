from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
