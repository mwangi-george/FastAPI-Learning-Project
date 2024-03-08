# -----------------base of the app lives here -------------------

from fastapi import FastAPI

# instantiate app
app = FastAPI()

# set up a route
@app.get("/")
