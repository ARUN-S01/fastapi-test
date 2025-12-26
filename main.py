from fastapi import FastAPI
from db import db

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Reply fromm server"}

@app.post("/items")
async def create_item(item: dict):
    result = await db.items.insert_one(item)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/items")
async def get_items():
    items = []
    async for item in db.items.find():
        item["_id"] = str(item["_id"])
        items.append(item)
    return items
