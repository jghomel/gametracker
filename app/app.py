import os

from flask import Flask, render_template, redirect
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for(go.__name__))


@app.route("/go", methods=['GET', 'POST'])
def go():
    if request.method == 'POST':
        champion = request.form['champion']
        set_champion(champion)
        app.logger.debug("New champion: {}".format(champion))
    else:
        champion = get_champion()
    return render_template('go.html', name=champion)


def get_champion():
    with open('/data/champion', 'r') as _file:
            champion = _file.read()
    return champion


def set_champion(champion):
    with open('/data/champion', 'w') as _file:
        _file.write(champion)


if __name__ == "__main__":
    try:
        port = int(os.environ['PORT'])
    except KeyError:
        exit("Please set the PORT environment variable")
    app.run(host='0.0.0.0', port=port)
