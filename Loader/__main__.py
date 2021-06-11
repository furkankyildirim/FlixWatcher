from Database import dbSelect, dbExecute
from bs4 import BeautifulSoup
from .setParams import setParams
import requests
import json
import sys


class Loader:
    @classmethod
    def getMoviesWillDelete(cls, code):
        params = setParams(code)
        content = requests.get(params["willDelete"], headers={"User-Agent": "XY"}).content
        soup = BeautifulSoup(content, 'html.parser')
        data = json.loads(soup.find('script', type='application/ld+json').string)

        for movie in data:
            movie = {
                "id": movie['url'][(movie['url'].rfind('-') + 1):],
                "Name": movie["name"],
                "endDate": movie["endDate"],
                "webLink": movie["url"],
                "Location": params["code"]
            }

            cls.saveMovieToDb(movie, params["code"])

    @classmethod
    def refreshMovies(cls, code):
        params = setParams(code)
        data = dbSelect("Select * from Movies", ())

        titles = ["id", "Name", "Description", "Type", "Year", "Rating", "Director", "Genres",
                  "Image", "startDate", "endDate", "webLink", "netflixLink", "Duration", "Persons", "Location"]

        for i in data:
            movie = dict(zip(titles, i))
            cls.saveMovieToDb(movie, params["code"])

    @classmethod
    def getNewMovies(cls, code):
        params = setParams(code)
        content = requests.get(params["newMovies"], headers={"User-Agent": "XY"}).content
        soup = BeautifulSoup(content, 'html.parser')
        data = soup.find_all("a", attrs={"class": "item-init"})

        for i in data:
            movie = {
                "id": i.get("href")[(i.get("href").rfind('-') + 1):],
                "Name": i.get("data-title"),
                "endDate": None,
                "webLink": params["url"] + i.get("href"),
                "Location": params["code"]
            }

            cls.saveMovieToDb(movie, params["code"])

    @classmethod
    def saveMovieToDb(cls, movie: dict, code: str):
        params = setParams(code)
        try: 
            if len(dbSelect("Select * from Movies where id = %s and Location = %s", (movie["id"], params["code"]))) == 0:
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
                    for item in soup.select(params["hrefMovies"]):
                        genres.append(item.text)
                    genres.pop()

                elif movie["Type"] == "TVSeries":
                    for item in soup.select(params["hrefSeries"]):
                        genres.append(item.text)
                    genres.pop(1)

                movie["Genres"] = ", ".join([n for n in genres])
                movie["Duration"] = soup.find("span", attrs={"class": "sub"}).text.split(" ")[2]
                temp = soup.find("h1").text
                movie["Year"] = temp[(temp.find("(") + 1):temp.find(")")]

                print(movie)
                movie["Image"] = requests.get(data["image"]).content

                preview = {
                    "id": movie["id"],
                    "Name": movie["Name"],
                    "Type": movie["Type"],
                    "Year": movie["Year"],
                    "Image": movie["Image"],
                    "Location": movie["Location"]
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
                            "webLink": params["url"] + item.get("href"),
                            "Movies": json.dumps([movie["id"]]),
                            "Name": item.get("href")[item.get("href").find("p/") + 2:item.get("href").rfind('-')]
                            }

                    person["netflixLink"] = "https://www.netflix.com/browse/m/person/" + str(person["id"])
                    person["Name"] = person["Name"].replace("-", " ").title()
                    cls.savePersonToDb(person, params["code"])

            elif movie["endDate"] is not None:
                dbExecute("Update Movies set endDate = %s where id = %s and Location = %s", (movie["endDate"], movie["id"], movie["Location"]))

            else:
                content = requests.get(movie["webLink"], headers={"User-Agent": "XY"}).content
                soup = BeautifulSoup(content, 'html.parser')

                for item in soup.select('a[href^="/p/"]'):
                    person = {"id": item.get("href")[(item.get("href").rfind('-') + 1):],
                            "webLink": params["url"] + item.get("href"),
                            "Movies": json.dumps([movie["id"]]),
                            "Name": item.get("href")[item.get("href").find("p/") + 2:item.get("href").rfind('-')]
                            }

                    person["netflixLink"] = "https://www.netflix.com/browse/m/person/" + str(person["id"])
                    person["Name"] = person["Name"].replace("-", " ").title()
                    cls.savePersonToDb(person, params["code"])
                    
        except:
            pass

    @classmethod
    def savePersonToDb(cls, person: dict, code: str):
        try:
            params = setParams(code)
            selection = dbSelect("Select * from Persons where id = %s", (person["id"],))

            if len(selection) == 0:
                print(person)
                query = "Insert into Persons (" + ",".join(
                    ["`" + n + "`" for n in person.keys()]) + ") VALUES (" + ",".join(
                    ["%s" for s in person.keys()]) + ");"

                dbExecute(query, tuple(list(person.values())))
                content = requests.get(person["webLink"], headers={"User-Agent": "XY"}).content
                soup = BeautifulSoup(content, 'html.parser')
                movies = soup.find_all("a", attrs={"class": "item-init item"})

                for i in movies:
                    movie = {
                        "id": i.get("href")[(i.get("href").rfind('-') + 1):],
                        "Name": i.get("data-title"),
                        "endDate": None,
                        "webLink": params["url"] + i.get("href"),
                        "Location": params["code"]
                    }

                    cls.saveMovieToDb(movie, params["code"])
            else:
                movie = json.loads(person["Movies"])[0]
                if movie not in json.loads(selection[0][2]):
                    person["Movies"] = json.loads(selection[0][2])
                    person["Movies"].append(movie)
                    dbExecute("Update Persons set Movies = %s where id = %s", (json.dumps(person["Movies"]), person["id"]))
                print(person)

        except:
            pass


class Cursor:

    @classmethod
    def getAllMovies(cls) -> list:
        sql = "Select * from Movies;"
        return dbSelect(sql, ())

    @classmethod
    def getMovies(cls, query: str, params: str) -> list:
        query = "Select * from Movies where {} = %s;".format(query)
        return dbSelect(query, (params,))


sys.setrecursionlimit(10000)
#: Sample
Loader().getMoviesWillDelete("us")
