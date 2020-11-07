import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
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
    # this function is to display the game on the main page and sort by upvote
    games = list(mongo.db.games.find().sort('upvote', pymongo.DESCENDING))
    return render_template("games.html", games=games)


@app.route("/search", methods=["GET", "POST"])
def search():
    # use this function to search for game
    query = request.form.get("query")
    games = list(mongo.db.games.find({"$text": {"$search": query}}))
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

    # then use the session user display all reviews by that user
    if session["user"]:
        games = mongo.db.games.find({'created_by': session["user"]})
        return render_template("profile.html", username=username, games=games)

    return redirect(url_for("login"))


@app.route("/delete_profile/<username>", methods=["GET", "POST"])
def delete_profile(username):
    # this gets the sessions users name
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # then delete that session user from db and all reviews by that user
    if session["user"]:
        games = mongo.db.games.delete_many({'created_by': session["user"]})
        user = mongo.db.users.delete_one({'username': session["user"]})
        session.clear()
        flash("Your Profile and All Reviews have been Deleted!")
        return redirect(url_for(
            "get_games", games=games, user=user, username=username))


@app.route("/logout")
def logout():
    # this function will log the user out
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/review/<game_id>', methods=['GET', 'POST'])
def review(game_id):
    # function to display the review when viewed.
    game = mongo.db.games.find_one({'_id': ObjectId(game_id)})

    return render_template('review.html', game=game)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        amazon_link = create_amazon_search(request.form.get("game_name"))

        # use this to create a new db entry for this review
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

        # use this to edit a review from the db
        review = {
            "game_name": request.form.get("game_name"),
            "game_developer": request.form.get("game_developer"),
            "genre_name": request.form.get("genre_name"),
            "game_description": request.form.get("game_description"),
            "game_review": request.form.get("game_review"),
            "game_image": request.form.get("game_image"),
            "created_by": session["user"],
            "amazon_link": amazon_link,
            }
        mongo.db.games.update({'_id': ObjectId(game_id)}, review)
        flash("Review successfully Updated!")
        game = mongo.db.games.find_one({'_id': ObjectId(game_id)})
        return render_template('review.html', game=game)

    game = mongo.db.games.find_one({'_id': ObjectId(game_id)})
    genre = mongo.db.genre.find().sort("genre_name", 1)
    return render_template("edit_review.html", game=game, genre=genre)


@app.route('/delete_review/<game_id>')
def delete_review(game_id):
    # this is the function to delete a review from the db
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Review successfully Deleted!")
    return redirect(url_for("get_games"))


@app.route("/upvote/<game_id>")
def upvote(game_id):
    # this is the function to increase the upvote.
    mongo.db.games.find_one_and_update(
        {"_id": ObjectId(game_id)}, {'$inc': {'upvote': 1}})
    return redirect(url_for('review', game_id=game_id))


@app.route("/get_genres")
def get_genres():
    # this is the function to display the genres from the db
    genre = list(mongo.db.genre.find().sort("genre_name", 1))
    return render_template("genres.html", genre=genre)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    # this function is to add a new genre to the db
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.insert_one(genre)
        flash("New Genre Added!")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    # this is to edit a genre from the db
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genre.update({'_id': ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated!")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genre.find_one({'_id': ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route('/delete_genre/<genre_id>')
def delete_genre(genre_id):
    # this is to delete the genre from the db
    mongo.db.genre.remove({"_id": ObjectId(genre_id)})
    flash("Genre successfully Deleted!")
    return redirect(url_for("get_genres"))


def create_amazon_search(game):
    # this fucntion allows the creation of an amazon link to search amazon

    amazonlink = 'https://www.amazon.co.uk/s?k='
    while ' ' in game:  # this replaces the spaces in the name with +
        game = game.replace(' ', '+')
    amazonlink += game

    return amazonlink  # returns the newly built amazon link


@app.errorhandler(404)
def page_not_found(e):
    # this is the route for handling 404 errors
    return render_template("404.html")


@app.errorhandler(400)
def bad_request(e):
    # this is the route for handling 400 errors
    return render_template("400.html")


@app.errorhandler(500)
def server_error(e):
    # this is the route for handling 500 errors
    return render_template("500.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
