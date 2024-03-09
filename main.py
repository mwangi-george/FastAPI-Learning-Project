# -----------------base of the app lives here -------------------

from fastapi import FastAPI
from enum import Enum  # for defining a fixed set of named values
from typing import Optional

# instantiate app
app = FastAPI()

# set up a route


@app.get("/")
async def root():
    return {"message": "Hello World!!"}

# on termial:
# uvicorn main:app --port=3000
# to allow live development, use the reload tag
# uvicorn main:app --reload

# Creating a post route


@app.post("/")
async def post():
    return {"message": "Hello from post route"}

# put route


@app.put("/")
async def put():
    return {"message": "Hello from put route"}


# Changing api param


@app.get("/user", description="This is a description about users")
async def get_user_info(name: str, email: str):
    return {"name": name, "email": email}


@app.get("/items")
async def list_items():
    return {"message": "List of items"}

# return a specific item, say by id 5
# http://localhost:8000/items/5

# the following shows a string


# @app.get("/items/{item_id}")
# async def get_items(item_id):
#     return {"item_id": item_id}

# http://localhost:8000/items/2000 returns
# {"item_id":"2000"}

# to retun id as an integer,
@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return {"item_id": item_id}


# to retun id as an integer,
@app.get("/names/{item_name}")
async def get_item_names(item_name: str):
    return {"item_id": item_name}


# order of routes matters
# specific end points must come before dynamic end points as follows


@app.get("/user_info/me")
async def get_user_info():
    return {"message": "this is the current user"}


@app.get("/user_info/{user_name}")
async def get_user_info(user_name: str):
    return {"message": f"the current user is {user_name}"}


class Foods(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_foods(food_name: Foods):
    if food_name == Foods.dairy:
        return {"food_name": food_name, "message": "Keep up the dairies"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "You are supper healthy"
        }
    return {
        "food_name": food_name,
        "message": f"{food_name} is great too"
    }


# query parameters
fake_items_db = [
    {"item_name": "faa"},
    {"item_name": "fee"},
    {"item_name": "fii"},
    {"item_name": "foo"},
    {"item_name": "fuu"},
    {"item_name": "baa"},
    {"item_name": "bee"}
]


@app.get("/list_items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# in the browser
# http://localhost:8000/list_items?limit=2
# http://localhost:8000/list_items?skip=2


# optional parameters
@app.get("/users/{user_id}")
async def get_user_info(user_id: int, q: Optional[str] = None):
    if q:
        return {"user_id": user_id, "query": q}
    return {"user_id", user_id}

my_info = {
    "name": "George",
    "height": 178,
    "email": "george178@yahoo.com"
}


@app.get("/api")
async def get_my_info(q: Optional[str] = None):
    if q in my_info.keys():
        return my_info[q]
