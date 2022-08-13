from fastapi import FastAPI
from fastapi.requests import Request

app = FastAPI()

@app.get('/')
def main(request:Request,file):
    print(request)
