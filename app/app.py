import os

from flask import Flask, render_template, redirect
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# This has to be after db creation for alembic to work properly
import models


@app.route('/')
def root():
    return redirect(url_for(go.__name__))


@app.route('/players')
def list_players():
    text = ""
    players = models.Player.query.all()
    for player in players:
        text += str(player) + '\n'
    return text


@app.route('/config')
def config():
    config = ""
    for key, value in app.config.items():
        config += "<div>"
        config += "{}: {}".format(key, value)
        config += "</div>"
    return config


@app.route("/go", methods=['GET', 'POST'])
def go():
    if request.method == 'POST':
        champion_name = request.form['champion']
        player_id = models.Player.query.filter_by(username=champion_name).first().id
        go = models.Game.query.filter_by(name='go').first()
        go.champion_id = player_id
        db.session.commit()
        app.logger.debug("New champion: {}".format(champion_name))
    else:
        go = models.Game.query.filter_by(name='go').first()
        try:
            champion_name = go.champion.username
        except AttributeError:
            champion_name = 'Personne'

    return render_template('go.html', name=champion_name)


if __name__ == "__main__":
    port = int(app.config['PORT'])
    app.run(host='0.0.0.0', port=port)
