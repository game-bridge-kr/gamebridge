import uvicorn
from fastapi import FastAPI
from .routers import user
from .routers import vultr
from .repository.mongo import database


app = FastAPI()


@app.on_event("startup")
def connect_mongodb():
    database.connect()

@app.on_event("shutdown")
def close_mongodb():
    database.close()


app.include_router(user.router)
app.include_router(vultr.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)