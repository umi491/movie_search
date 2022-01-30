import requests
import configparser
from flask import Flask

app = Flask(__name__)

@app.route('/')
def movie_dashboard():
    return render_template('home.html')

def get_movie_results(movie_title):
    api_url = "https://imdb-api.com/API/SearchAl/k_yz9612sh/?title={}".format(movie_title)
    print(api_url)

get_movie_results("inception")