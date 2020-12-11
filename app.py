from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World"}


@app.get("/delay/{sec}")
def get_delay(sec: int):
    """
    sec秒遅延させる
    """
    requests.get("https://httpbin.org/delay/{}".format(sec))
    return {"sec": sec}


@app.post("/anything")
def post_anything():
    """
    情報を返す
    """
    r = requests.post("https://httpbin.org/anything")
    return r.json()
