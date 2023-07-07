from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"data": "hello world!"}


if __name__ == '__main__':
    uvicorn.run("app:app", port=1111, host='127.0.0.1')

