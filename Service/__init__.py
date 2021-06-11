from flask import Flask, request, jsonify
from configparser import ConfigParser
from .main import Connection

#: Get Configs
config = ConfigParser()
config.read("./config.ini")
app = Flask(__name__)


# method: index
# Testing for flask installation
# @completed
@app.route('/')
def index():
    return jsonify(Home='Welcome')


# method: willDeleted
# Get the movie which will be deleted
# @completed
@app.route('/api/v1/willdeleted')
def willDeleted():
    cc = request.args.get('cc', None)
    movies = Connection.willDeleted(cc)
    return jsonify(movies)


# method: getAllMovies
# Get the all movies
# @completed
@app.route('/api/v1/allmovies', methods=['GET'])
def getAllMovies():
    movies = Connection.getAllMovies()
    return jsonify(movies)


# method: getMovie
# Get the movie which you want by movie id
# @completed
@app.route('/api/v1/movie', methods=['GET'])
def getMovie():
    _id = request.args.get('id', None)
    cc = request.args.get('cc', None)

    if _id is not None:
        movie = Connection.getMovie(_id, cc)
        return jsonify(movie)
    else:
        return jsonify({'type': 'error', 'output': 'no parameter is supplied'})


# method: getPerson
# Get the person which you want by person id or movie id
# @completed
@app.route('/api/v1/person', methods=['GET'])
def getPerson():
    _id = request.args.get('id', None)
    movie = request.args.get('movie', None)
    cc = request.args.get('cc', None)

    if _id is not None:
        person = Connection.getPersonById(_id, cc)
        return jsonify(person)

    elif movie is not None:
        person = Connection.getPersonsByMovieId(movie, cc)
        return jsonify(person)

    else:
        return jsonify({'type': 'error', 'output': 'no parameter is supplied'})


if __name__ == "__main__":
    app.run(
        host=config["Service"]["host"],
        port=int(config["Service"]["port"])
    )
