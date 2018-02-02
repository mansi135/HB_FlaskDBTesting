from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    Game.query.delete()

    g1 = Game(game_id=1, name="Catan", description="Play endless")
    g2 = Game(game_id=2, name="Poker", description="Play whole night")
    g3 = Game(game_id=3, name="Mafia", description="You will like it")
    g4 = Game(game_id=4, name="Checker", description="Checks checks")

    db.session.add_all([g1, g2, g3, g4])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
