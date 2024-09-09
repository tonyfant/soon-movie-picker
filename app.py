from flask import Flask, render_template, request, redirect, url_for
from user import User
from movie import Movie
import api_util

app = Flask(__name__)

active_users = {}
iteration = 0
movies_visited=[]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        nationality = request.form['nationality']
        subscriptions = request.form.getlist('subscriptions')
        
        subscriptions = list(map(int, subscriptions))
        
        user = User(username, nationality, subscriptions)
        active_users[username] = user
        
        return redirect(url_for('recommend_movie', username=username))
    
    providers = {8:"Netflix",
                 175 : "Netflix Kids",
                 1796 : "Netflix basic with Ads",
                 9 : "Amazon Prime Video",
                 2100 : "Amazon Prime Video with Ads",
                 337 : "Disney Plus",
                 39 : "Now TV",
                 531 : "Paramount Plus",
                 109: "Timvision",
                 510 : "Discovery+",
                 210 : "Sky"
                 
                 
                  }
    return render_template('home.html', providers=providers)

@app.route('/recommend/<username>')
def recommend_movie(username):
    user = active_users.get(username)
    if not user:
        return redirect(url_for('home'))
    while True:
        movie = api_util.recommend_movie(user)
        if movie and not movie.id in movies_visited:
            movies_visited.append(movie.id)
            return render_template('recommendation.html', movie=movie, username=username)

    return "No movie could be recommended at this time."

@app.route('/like/<username>/<int:movie_id>')
def like_movie(username, movie_id):
    user = active_users.get(username)
    if user:
        movie_genres = api_util.get_movie_genres(movie_id)
        user.update_preferences(genres_liked=movie_genres, genres_disliked=[], like=True)
    return redirect(url_for('recommend_movie', username=username))

@app.route('/dislike/<username>/<int:movie_id>')
def dislike_movie(username, movie_id):
    user = active_users.get(username)
    if user:
        movie_genres = api_util.get_movie_genres(movie_id)
        user.update_preferences(genres_liked=[], genres_disliked=movie_genres, like=False)
    return redirect(url_for('recommend_movie', username=username))


if __name__ == '__main__':
    app.run(debug=True)
