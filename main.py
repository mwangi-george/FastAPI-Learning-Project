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

user_name = "John Doe"
user_email = "john_doe@gmail.com"

# Changing api param


@app.get("/user", description="This is a description about users", deprecated=True)
async def get_user_info(name: str, email: str):
    return {"name": user_name, "email": user_email}
