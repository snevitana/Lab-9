from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Game store')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# products = [
#     {'prod_name': 'sofa',
#      'price': 12000,
#      'in_stock': False,
#      'id': 0},
#     {'prod_name': 'table',
#      'price': 6000,
#      'in_stock': True,
#      'id': 1},
#     {'prod_name': 'chair',
#      'price': 8000,
#      'in_stock': False,
#      'id': 2},
# ]


class Game(db.Model):
    game_name = db.Column(db.String(300))
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'Game{self.id}. {self.game_name} - {self.year}'

@app.route('/')
def main():
    games = Game.query.all()
    return render_template('index.html', games_list=games)


@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    game = Game(**data)
    db.session.add(game)
    db.session.commit()

    return 'OK'


@app.route('/clear', methods=['DELETE'])
def clear():
    db.session.query(Game).delete()
    db.session.commit()
    return 'OK'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)