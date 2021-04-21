

from flask import Flask, request, render_template

import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "OK béla"
    else:
        with open("todos.json", "r") as f:
            todos = json.load(f)
        return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run()
