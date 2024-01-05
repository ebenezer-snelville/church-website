from flask import Flask

app = Flask(__name__)


@app.route("/")
def cw_index():
    # TODO: Return HTML instead
    return "<p>Hello, World!</p>"
