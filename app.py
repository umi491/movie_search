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
    json_data = get_movies(movie_title)
    return render_template('results.html', data=json_data["results"])


if __name__ == '__main__':
    app.run(debug=True)


def get_movies(movie_title):
    api_url = "https://imdb-api.com/en/API/SearchMovie/k_yz9612sh/{}".format(movie_title)
    r = requests.get(api_url)
    return r.json()