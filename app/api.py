from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def roo():
    return {"message": "BSPI HELLO WORLD"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
