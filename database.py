from model import Player
import os

import motor.motor_asyncio

mongodb_url = os.environ["MONGODB_URL"]

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_url)
database = client.db0
collection = database.collection0

async def create_player(player):
    document = player
    result = await collection.insert_one(document)
    return document

async def fetch_player_with_name(name):
    document = await collection.find_one({"name": name})
    return document
    