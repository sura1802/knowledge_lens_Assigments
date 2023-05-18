from fastapi import FastAPI

app = FastAPI()


@app.post('/Addition/{x}/{y}')
async def addition(x: int, y: int):
    return {"Addition is:": x + y}


@app.post('/Subtraction')
async def subtraction(x: int, y: int):
    return {"Addition is:": x - y}


@app.post('/Multiplication')
async def multiplication(x: int, y: int):
    return {"Addition is:": x * y}


@app.post('/Division')
async def division(x: int, y: int):
    return {"Division is:": x / y}
