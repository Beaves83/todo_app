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
    cursor = db_connection.cursor()

    get_query = "SELECT * FROM items ORDER BY id"
    cursor.execute(get_query)

    items = []
    for row in cursor.fetchall():
        item = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "completed": row[3],
        }
        items.append(item)

    cursor.close(); 
    return items

@app.post("/items")
async def create_item(item: dict):
    cursor = db_connection.cursor()

    insert_query = "INSERT INTO items (title, description) VALUES (%s, %s)"
    cursor.execute(insert_query, (item["title"], item["description"]))

    db_connection.commit()
    cursor.close()
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