# --- Flask Hello World --- #

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello World???!"

@app.route("/search/<search_query>")
def search(search_query):
    return "Hello " + search_query

@app.route("/integer/<int:value>")
def int_type(value):
    if value < 100:
        print value + 1
        return "Thats not a very big number"
    else:
        print value + 1
        return "Thats a big number"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "It's a float"

@app.route("/path/<path:value>")
def path_value(value):
    print value
    return "hello " + value

@app.route("/name/<name>")
def index(name):
    if name.lower() == "clark":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
