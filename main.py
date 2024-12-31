from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"message": "hello"}

@app.get("/items")
def get_items():
    return {"message": "items"}