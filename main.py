from fastapi import FastAPI, HTTPException
from model import Player
from database import create_player, fetch_player_with_name

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/player", response_model=Player)
async def post_player(player: Player):
    response = await create_player(player.dict())
    if response:
        return response
    raise HTTPException(400, "bad request")

@app.get("/api/player{name}", response_model=Player)
async def get_player_with_name(name: str):
    response = await fetch_player_with_name(name)
    if response:
        return response
    raise HTTPException(404, f"404 not found: {name}")
