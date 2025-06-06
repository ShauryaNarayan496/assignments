from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the expected JSON structure
class User(BaseModel):
    name: str
    age: int

@app.post("/transform")
def transform_user(user: User):
    # Transform the data
    uppercase_name = user.name.upper()
    greeting = f"Hello, {uppercase_name}! You are {user.age} years old."

    return {
        "original": user,
        "transformed": {
            "name_upper": uppercase_name,
            "greeting": greeting
        }
    }
