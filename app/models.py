from app import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    champion_of = db.relationship('Game', backref='champion', lazy=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return 'id {}, user {}'.format(self.id, self.username)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    champion_id = db.Column(db.Integer, db.ForeignKey('player.id'))

    def __init__(self, name, champion_id=None):
        self.name = name
        self.champion_id = champion_id

    def __repr__(self):
        return 'id {}, name {}, champion: {}'.format(self.id, self.name, self.champion_id)
