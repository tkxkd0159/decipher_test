from flask import Flask, render_template, request
from flask_jsonrpc import JSONRPC
from lib import checkName, makeSeed, makeUniqueID

app = Flask(__name__)
rpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/seed", methods=['POST'])
def getSeed() -> str:
    req = request
    if req.headers['Content-Type'] == "application/json":
        req = req.json
        name: str = req["name"]
        if not checkName(name):
            return "Please follow the given name form"
        elif name == "SatoshiNakamoto":
            return "Use your own name"
        age: int = req["age"]
        if type(age) is not int:
            return "Please follow the given age form"

    else:
        return "Please check your request type"

    seed = makeSeed(name, age)
    res = f'Your seed : {seed}'

    return res

@rpc.method('genUniqueID')
def getID(name: str, age: int, seed: str) -> str:
    res = makeUniqueID(name, age, seed)
    return f'Success!!! Your ID : {res}'


if __name__ == "__main__":
    app.run()