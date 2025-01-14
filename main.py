from flask import Flask

app = Flask(__name__)

text = "Hola Mundo"

@app.route("/", methods=["GET"])
def home():
    return f"<h1>{text}</h1>"


@app.route("/greeting", methods=["GET"])
def home():
    return "Hola Mundo"

if __name__:
    app.run(port=3000, debug=True)