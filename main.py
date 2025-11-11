from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_root():
    return {"Root URL message": "Welcome to FastAPI sample project Home page"}

@app.get("/about")
def get_about():
    return {"data": {"message": "More about this FastAPI app"}}