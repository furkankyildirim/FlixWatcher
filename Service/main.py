from Database import dbSelect
from base64 import encodebytes
from datetime import date
import json


class Connection:

    # method: __setMovieResponse
    # Edit movie to send the client
    # @movie, list: The movie which you want to edit
    # @return, dict: Edited movie for sending the client
    # @completed
    @staticmethod
    def __setMovieResponse(movie: list) -> dict:
        #: Define response key
        titles = ["id", "Name", "Description", "Type", "Year", "Rating", "Director", "Genres", "Image",
                  "startDate", "endDate", "webLink", "netflixLink", "Duration", "Persons", "Location"]

        #: Edit image format
        movie[8] = encodebytes(movie[8]).decode()

        #: Set duration type
        movie[13] = movie[3] == "Movie" and (movie[13] + " minutes") or movie[13] + " season(s)"

        #: Create response
        response = dict(zip(titles, movie))

        #: return response
        return response

    # method: __setPreviewResponse
    # Edit all previews to send the client
    # @movie, list: The movie which you want to edit
    # @return, dict: Edited movie for sending the client
    # @completed
    @staticmethod
    def __setPreviewResponse(movie: list) -> dict:
        #: Define response key
        titles = ["id", "Name", "Type", "Year", "Image", "Location"]

        #: Edit image format
        movie[4] = encodebytes(movie[4]).decode()

        #: Create response
        response = dict(zip(titles, movie))

        #: return response
        return response

    # method: __setPersonsResponse
    # Edit persons to send the client
    # @person, list: The person id which you want to edit
    # @return, dict: Edited person for sending the client
    # @completed
    @staticmethod
    def __setPersonsResponse(person: list) -> dict:
        #: Define response key
        titles = ["id", "Name"]

        #: Create response
        response = dict(zip(titles, person))

        #: return response
        return response

    # method: __setPersonResponse
    # Edit person to send the client
    # @person, list: The person id which you want to edit
    # @return, dict: Edited person for sending the client
    # @completed
    @staticmethod
    def __setPersonResponse(person: list) -> dict:
        #: Define response key
        titles = ["id", "Name", "Movies", "webLink", "netflixLink", "Location"]

        #: Create response
        response = dict(zip(titles, person))

        #: Edit Movies format
        response["Movies"] = json.loads(response["Movies"])

        #: return response
        return response

    # method: getAllMovies
    # Get all movies from Preview db without param
    # @return, list: The list of all movies
    # @completed
    @classmethod
    def getAllMovies(cls) -> list:
        #: Set Query
        sql = "Select * from Preview;"

        #: Get All Movies from Db
        movies = dbSelect(sql, ())

        #: Edit All Movies Format
        for i in range(len(movies)):
            movie = list(movies[i])
            movies[i] = cls.__setPreviewResponse(movie)

        #: Return All Movies
        return movies

    # method: getPersonsByMovieId
    # Get persons from database by movie id
    # @movieId: The movie id which you want to get persons
    # @cc: The country code
    # @return, list: The list of matching item
    # @completed
    @classmethod
    def getPersonsByMovieId(cls, movieId: str, cc: str) -> list:
        #: Set Query
        param = '%{}%'.format(movieId)
        sql = "Select id, Name from Persons where Location = %s and Movies Like %s;"

        #: Get Persons who played in movie
        persons = dbSelect(sql, (cc, param))

        #: Check Persons is exist by id
        if len(persons) == 0: return [{'type': 'error', 'output': 'no parameter is supplied'}]

        #: Edit Persons format
        for i in range(len(persons)):
            person = list(persons[i])
            persons[i] = cls.__setPersonsResponse(person)

        #: Return persons
        return persons

    # method: getPersonById
    # Get person from database by person id
    # @_id: The person id which you want
    # @cc: The country code
    # @return, dict: The list of matching item
    # @completed
    @classmethod
    def getPersonById(cls, _id: str, cc: str) -> dict:
        #: Set Query
        sql = "Select * from Persons where id = %s and Location = %s;"

        #: Get Person from Db
        person = dbSelect(sql, (_id, cc))

        #: Check Person is exist by id
        if len(person) == 0: return {'type': 'error', 'output': 'no parameter is supplied'}

        #: Edit Movie Format -> Dict
        person = cls.__setPersonResponse(list(person[0]))

        #: Get movie previews who person played in
        movies = []
        for i in range(len(person["Movies"])):
            movies.append(cls.getMoviePreview(str(person["Movies"][i]), cc))
        person["Movies"] = movies

        #: Return movie
        return person

    # method: getMovie
    # Get movie from database by id
    # @param: The movie id which you want
    # @cc: The country code
    # @return, dict: The dictionary of matching item
    # @completed
    @classmethod
    def getMovie(cls, param: str, cc: str) -> dict:
        #: Set Query
        query = "Select * from Movies where id = %s and Location = %s;"

        #: Get Movie from Db
        movie = dbSelect(query, (param, cc))

        #: Check Movie is exist by id
        if len(movie) == 0: return {'type': 'error', 'output': 'no parameter is supplied'}

        #: Edit Movie Format -> Dict
        movie = cls.__setMovieResponse(list(movie[0]))

        #: Get persons who played in movie
        persons = cls.getPersonsByMovieId(movie['id'], cc)
        movie['Persons'] = persons

        #: Return movie
        return movie

    # method: getMoviePreview
    # Get movie preview from database by id
    # @param: The movie id which you want
    # @cc: The country code
    # @return, dict: The dictionary of matching item
    # @completed
    @classmethod
    def getMoviePreview(cls, param: str, cc: str) -> dict:
        #: Set Query
        query = "Select * from Preview where id = %s and Location = %s;"

        #: Get Movie Preview from Db
        movie = dbSelect(query, (param, cc))

        #: Check Movie is exist by id
        if len(movie) == 0: return {'type': 'error', 'output': 'no parameter is supplied'}

        #: Edit Movie Preview Format -> Dict
        movie = cls.__setPreviewResponse(list(movie[0]))

        #: Return movie
        return movie

    # method: will
    # Get movie preview from database by id
    # @cc: The country code
    # @return, dict: The dictionary of matching item
    # @completed
    @classmethod
    def willDeleted(cls, cc: str) -> list:
        #: Set Query
        query = "Select id from Movies where endDate >= %s and Location = %s order by endDate;"

        #: Set date
        today = date.today().strftime('%Y-%m-%d')

        #: Get Movies Id from Db by Date
        moviesId = dbSelect(query, (today, cc))

        #: Check Movies are exist by id
        if len(moviesId) == 0: return [{'type': 'error', 'output': 'no parameter is supplied'}]

        #: Set response
        movies = []

        #: Get will be deleted movies by id
        for i in range(len(moviesId)):
            movie = cls.getMoviePreview(moviesId[i][0], cc)
            movies.append(movie)

        #: Return Movies Preview
        return movies
