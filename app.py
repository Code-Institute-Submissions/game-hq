import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_games")
def get_games():
    games = list(mongo.db.games.find())
    return render_template("games.html", games=games)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # first to check if the username already exists in the database?
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Exists!")
            return redirect(url_for("register"))

        # if no existing user is in the database then add user to db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # also need to put the new user into 'session' cookies
        session["user"] = request.form.get("username").lower()
        flash("Registration Was Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check is username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # if user exists then check the hashed password matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if the password entered is Invalid then flash user
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if the username does not exist then flash user
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the sessions username from the database for the session variable
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # this function will log the user out
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/review/<game_id>', methods=['GET', 'POST'])
def review(game_id):
    ''' function to return a single record of the review db
     on the basis of the id of the item in the collection,
     runs when 'view review' is clicked '''

    game = mongo.db.games.find_one({'_id': ObjectId(game_id)})
    
    return render_template('review.html', game=game)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        amazon_link = create_amazon_search(request.form.get("game_name"))

        game = {
            "game_name": request.form.get("game_name"),
            "game_developer": request.form.get("game_developer"),
            "genre_name": request.form.get("genre_name"),
            "game_description": request.form.get("game_description"),
            "game_review": request.form.get("game_review"),
            "game_image": request.form.get("game_image"),
            "created_by": session["user"],
            "amazon_link": amazon_link,
            "upvote": 0,
            }
        mongo.db.games.insert_one(game)
        flash("Review successfully Added!")
        return redirect(url_for("get_games"))

    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("add_review.html", genre=genre)


@app.route('/edit_review/<game_id>', methods=['GET', 'POST'])
def edit_review(game_id):
    if request.method == "POST":
        amazon_link = create_amazon_search(request.form.get("game_name"))

        review = {
            "game_name": request.form.get("game_name"),
            "game_developer": request.form.get("game_developer"),
            "genre_name": request.form.get("genre_name"),
            "game_description": request.form.get("game_description"),
            "game_review": request.form.get("game_review"),
            "game_image": request.form.get("game_image"),
            "amazon_link": amazon_link,
            }
        mongo.db.games.update({'_id': ObjectId(game_id)}, review)
        flash("Review successfully Updated!")

    game = mongo.db.games.find_one({'_id': ObjectId(game_id)})
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("review.html", game=game, genre=genre)


@app.route('/delete_review/<game_id>')
def delete_review(game_id):
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Review successfully Deleted!")
    return redirect(url_for("get_games"))


def create_amazon_search(game):
    # this fucntion allows the creation of an amazon link to search amazon

    amazonlink = 'https://www.amazon.co.uk/s?k='
    while ' ' in game:  # this replaces the spaces in the name with +
        game = game.replace(' ', '+')
    amazonlink += game

    return amazonlink  # returns the newly built amazon link


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
