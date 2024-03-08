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
