from dbConnection import dbSelect, dbExecute
from bs4 import BeautifulSoup
import requests
import json
import sys


class Loader:
    @classmethod
    def getMoviesWillDelete(cls):
        content = requests.get("https://turflix.com/kaldirildi",
                               headers={"User-Agent": "XY"}).content

        soup = BeautifulSoup(content, 'html.parser')
        data = json.loads(soup.find('script', type='application/ld+json').string)
        for movie in data:
            movie = {
                "id": movie['url'][(movie['url'].rfind('-') + 1):],
                "Name": movie["name"],
                "endDate": movie["endDate"],
                "webLink": movie["url"],
            }

            cls.saveMovieToDb(movie)

    @classmethod
    def saveMovieToDb(cls, movie: dict):
        if len(dbSelect("Select * from Movies where id = %s", (movie["id"],))) == 0:
            content = requests.get(movie["webLink"], headers={"User-Agent": "XY"}).content
            soup = BeautifulSoup(content, 'html.parser')
            data = json.loads(soup.find('script', type='application/ld+json').string)

            if "director" in data: movie["Director"] = data["director"]
            if "description" in data: movie["Description"] = data["description"]
            if "dateCreated" in data: movie["startDate"] = data["dateCreated"]
            if "@type" in data: movie["Type"] = data["@type"]
            if "aggregateRating" in data: movie["Rating"] = data["aggregateRating"]["ratingValue"]

            movie["netflixLink"] = "https://www.netflix.com/title/" + movie["id"]
            movie["Genres"], genres = "", []

            if movie["Type"] == "Movie":
                for item in soup.select('a[href^="/filmler"]'):
                    genres.append(item.text)
                genres.pop()

            elif movie["Type"] == "TVSeries":
                for item in soup.select('a[href^="/diziler"]'):
                    genres.append(item.text)
                genres.pop(1)

            movie["Genres"] = ", ".join([n for n in genres])
            movie["Duration"] = soup.find("span", attrs={"class": "sub"}).text.split(" ")[2]
            temp = soup.find("h1").text
            movie["Year"] = temp[(temp.find("(")+1):temp.find(")")]

            print(movie)
            movie["Image"] = requests.get(data["image"]).content

            preview = {
                "id": movie["id"],
                "Name": movie["Name"],
                "Type": movie["Type"],
                "Year": movie["Year"],
                "Image": movie["Image"],
            }

            query = "INSERT INTO Movies (" + ",".join(
                ["`" + n + "`" for n in movie.keys()]) + ") VALUES (" + ",".join(
                ["%s" for s in movie.keys()]) + ");"
            dbExecute(query, tuple(list(movie.values())))

            query = "INSERT INTO Preview (" + ",".join(
                ["`" + n + "`" for n in preview.keys()]) + ") VALUES (" + ",".join(
                ["%s" for s in preview.keys()]) + ");"
            dbExecute(query, tuple(list(preview.values())))

            for item in soup.select('a[href^="/p/"]'):
                person = {"id": item.get("href")[(item.get("href").rfind('-') + 1):],
                          "webLink": "https://turflix.com" + item.get("href"),
                          "Movies": json.dumps([movie["id"]]),
                          "Name": item.get("href")[item.get("href").find("p/") + 2:item.get("href").rfind('-')]
                          }

                person["netflixLink"] = "https://www.netflix.com/browse/m/person/" + str(person["id"])
                person["Name"] = person["Name"].replace("-", " ").title()
                cls.savePersonToDb(person)

    @classmethod
    def savePersonToDb(cls, person: dict):
        selection = dbSelect("Select * from Persons where id = %s", (person["id"],))

        if len(selection) == 0:
            print(person)
            query = "Insert into Persons (" + ",".join(
                ["`" + n + "`" for n in person.keys()]) + ") VALUES (" + ",".join(
                ["%s" for s in person.keys()]) + ");"

            dbExecute(query, tuple(list(person.values())))
            content = requests.get(person["webLink"], headers={"User-Agent": "XY"}).content
            soup = BeautifulSoup(content, 'html.parser')
            movies = soup.find_all("a",attrs={"class": "item-init item"})

            for i in movies:
                movie = {
                    "id": i.get("href")[(i.get("href").rfind('-') + 1):],
                    "Name": i.get("data-title"),
                    "endDate": None,
                    "webLink": "https://turflix.com" + i.get("href")
                }

                cls.saveMovieToDb(movie)
        else:
            movie = json.loads(person["Movies"])[0]
            if movie not in json.loads(selection[0][2]):
                person["Movies"] = json.loads(selection[0][2])
                person["Movies"].append(movie)
                dbExecute("Update Persons set Movies = %s where id = %s", (json.dumps(person["Movies"]), person["id"]))
            print(person)


class Cursor:
    def __init__(self):
        pass

    def getAllMovies(self) -> list:
        sql = "Select * from Movies;"
        return dbSelect(sql, ())

    def getMovies(self, query: str, params: str) -> list:
        query = "Select * from Movies where {} = %s;".format(query)
        return dbSelect(query, (params,))


sys.setrecursionlimit(10000)
Loader.getMoviesWillDelete()
