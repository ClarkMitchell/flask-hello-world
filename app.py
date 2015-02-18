# --- Flask Hello World --- #

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/phil")
def phil():
    return "Hello Phil"

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

if __name__ == "__main__":
    app.run()
