import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def search_home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def search_results():
    movie_title = request.form['movieTitle']
    data = get_movies(movie_title)

    title = data["Title"]
    released = data["Released"]
    genre = data["Genre"]

    return render_template('results.html', title=title, released=released, genre=genre)


if __name__ == '__main__':
    app.run(debug=True)


def get_movies(movie_title):
    api_url = "http://www.omdbapi.com/?t={}&apikey=3507e773".format(movie_title)
    r = requests.get(api_url)
    return r.json()