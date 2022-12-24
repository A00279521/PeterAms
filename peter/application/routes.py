# from application import app, crud_db
# from application.models import Games
# from flask import request, redirect, url_for

# @app.route('/home', methods=["GET","POST"])
# def hello_internet():
#     if request.method == "POST":
#          return "2Hello Internet!"
#     else:
#         return "This is a  method"

# @app.route('/add')
# def add():
#     new_game = Games(name="New Game")
#     crud_db.session.add(new_game)
#     crud_db.session.commit()
#     return "Added new game to database"

# @app.route('/read')
# def read():
#     all_games = Games.query.all()
#     games_string = ""
#     for game in all_games:
#         games_string += "<br>"+ game.name
#     return games_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     crud_db.session.commit()
#     return first_game.name

