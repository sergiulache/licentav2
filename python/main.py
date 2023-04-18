from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# server start command: uvicorn main:app --reload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/calculate_winner")
async def calculate_winner(data: dict):
    # Implement your algorithm here
    # set winner equal to data
    winner = {}
    winner["ane"] = data["data"].upper()
    winner["pula"] = "pula"

    return {"winner": winner}
