

from flask import Flask, request, render_template

import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with open("todos.json", "r") as f:
            tmp = json.load(f)
            tmp.append({"userId": 10, "id": 999,
                       "title": request.form["title"], "completed": False})

        with open("todos.json", "w") as f:
            json.dump(tmp, f)

        return "ok"
    else:
        with open("todos.json", "r") as f:
            todos = json.load(f)
        return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run()
