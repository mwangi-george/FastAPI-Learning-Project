# -----------------base of the app lives here -------------------

from fastapi import FastAPI

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
