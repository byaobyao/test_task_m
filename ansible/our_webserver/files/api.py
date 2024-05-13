#!/usr/bin/python
from fastapi import FastAPI

# creating API
app = FastAPI()


# default route
@app.get("/")
async def root():
    return {
            "Pong"
    }

