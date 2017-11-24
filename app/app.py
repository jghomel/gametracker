import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    try:
        port = int(os.environ['PORT'])
    except KeyError:
        exit("Please set the PORT environment variable")
    app.run(host='0.0.0.0', port=port)
