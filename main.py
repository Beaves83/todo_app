from fastapi import FastAPI 
import psycopg2

app = FastAPI()

db_connection = psycopg2.connect(
    host="localhost",
    port="5432",
    user="root",
    password="root",
    database="todo_app"
)

@app.get("/items")
async def get_items():
    items = []
    return items

@app.post("/items")
async def create_item(item: dict):
    return {"message": "Item created successfully"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"message": f"Item {item_id} updated successfully"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)