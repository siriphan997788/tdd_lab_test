from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "natthanan"}

@app.post("/")
def read_root():
    return {"hello": "natthanan post"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname/")
def read_name(name: str = None):
    return {"hello": name}


handler = Mangum(app)
