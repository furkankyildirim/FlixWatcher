from Database import dbSelect, dbExecute
from bs4 import BeautifulSoup
from random import randint
from .setParams import setParams
import requests
import json
import sys
import datetime


class Loader:

    @classmethod
    def getPopularMovies(cls, code: str):
        params = setParams(code)
        content = requests.get(params["popularMovies"], headers={"User-Agent": "XY"}).content
        soup = BeautifulSoup(content, 'html.parser')
        movies = soup.find_all("div", attrs={"class": "card-header card-header-image"})

        for i in movies:
            href = i.find("a").get("href")
            movie = {
                "webLink": params["url"] + href,
                "endDate": None,
                "Location": params["code"]
            }

            cls.saveMovieToDb(movie, params["code"])

    @classmethod
    def getNewMovies(cls, code: str):
        params = setParams(code)
        content = requests.get(params["url"], headers={"User-Agent": "XY"}).content
        soup = BeautifulSoup(content, 'html.parser')
        movies = soup.find_all("div", attrs={"class": "card-header card-header-image"})

        for i in movies:
            href = i.find("a").get("href")
            movie = {
                "webLink": params["url"] + href,
                "endDate": None,
                "Location": params["code"]
            }

            cls.saveMovieToDb(movie, params["code"])

    @classmethod
    def getMoviesWillDelete(cls, code: str):
        params = setParams(code)
        for i in range(1, 4):
            content = requests.get((params["willDelete"] + str(i)), headers={"User-Agent": "XY"}).content
            soup = BeautifulSoup(content, 'html.parser')
            data = soup.find_all('div', attrs={"class": "row"})

            for index in range(4, len(data) - 2):
                item = data[index].find("h3")
                if item is not None:
                    date = item.text.strip().split(".")
                    date = str(datetime.datetime.now().year) + "-" + date[1] + "-" + date[0]
                else:
                    items = data[index].find_all("a")
                    for j in range(0, len(items), 2):
                        movie = {
                            "webLink": params["url"] + items[j].get("href"),
                            "endDate": date,
                            "Location": code
                        }

                        cls.saveMovieToDb(movie, code)

    @classmethod
    def saveMovieToDb(cls, movie: dict, code: str):
        params = setParams(code)

        try:
            if len(dbSelect("Select * from Movies where webLink = %s and Location = %s", (movie["webLink"], params["code"]))) == 0:
                content = requests.get(movie["webLink"], headers={"User-Agent": "XY"}).content
                soup = BeautifulSoup(content, 'html.parser')

                movie["Name"] = soup.find("h1").text
                movie["Year"] = soup.find_all("span", attrs={"class": "mr-2"})[0].text
                movie["Duration"], temp = soup.find_all("span", attrs={"class": "mr-2"})[2].text.split(" ")
                movie["Type"] = "Movie" if temp == "dk." else "TVSeries"
                movie["Description"] = soup.find("p", attrs={"class": "card-description text-white"}).text
                movie["Rating"] = soup.find("span", attrs={"class": "fas fa-star rating mr-1"}).nextSibling.text.split("/")[0]
                movie["startDate"] = soup.find_all("span", attrs={"class": "mr-2"})[-1].nextSibling.text.split(".")
                movie["startDate"] = movie["startDate"][2] + "-" + movie["startDate"][1] + "-" + movie["startDate"][0]
                movie["Director"] = soup.find_all("span", attrs={"class": "mr-2"})[4].nextSibling.text
                movie["Location"] = code

                movie["Genres"], genres = "", []
                for item in soup.find_all("span", attrs={"class": "mr-2"})[3].parent.find_all("a"):
                    genres.append(item.text)
                movie["Genres"] = ", ".join([n for n in genres])

                if "endDate" not in movie: movie["endDate"] = None

                scriptId = soup.find_all("script")[-1].string
                scriptId = scriptId[scriptId.find("id:"):]
                movie["id"] = scriptId[5:scriptId.find(",") - 1]
                movie["netflixLink"] = "https://www.netflix.com/title/" + movie["id"]

                print(movie)
                movie["Image"] = requests.get(soup.find("img").get("data-src")).content

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

                for item in soup.select('a[href^="/director/"]'):
                    person = {
                        "Name": item.text, "Movies": json.dumps([movie["id"]]), "netflixLink": None,
                        "webLink": params["url"] + item.get("href"), "Location": params["code"],
                    }

                    cls.savePersonToDb(person, params["code"])

                for item in soup.select('a[href^="/actor/"]'):
                    person = {
                        "Name": item.text, "Movies": json.dumps([movie["id"]]), "netflixLink": None,
                        "webLink": params["url"] + item.get("href"), "Location": params["code"],
                    }

                    cls.savePersonToDb(person, params["code"])

                movies = soup.find_all("div",attrs={"class": "card-header card-header-image"})

                for i in movies:
                    href = i.find("a").get("href")
                    movie = {
                        "webLink": params["url"] + href,
                        "endDate": None,
                        "Location": params["code"]
                    }

                    cls.saveMovieToDb(movie, params["code"])

            elif movie["endDate"] is not None:
                dbExecute("Update Movies set endDate = %s where webLink = %s and Location = %s",
                          (movie["endDate"], movie["webLink"], movie["Location"]))
        except:
            pass


    @classmethod
    def savePersonToDb(cls, person: dict, code: str):
        try:
            params = setParams(code)
            selection = dbSelect("Select * from Persons where webLink = %s and Location = %s", (person["webLink"], params["code"]))

            if len(selection) == 0:
                print(person)

                while True:
                    person["id"] = randint(10000000, 99999999)
                    if len(dbSelect("Select * from Persons where id = %s and Location = %s",(person["webLink"], params["code"]))) == 0:
                        break

                query = "Insert into Persons (" + ",".join(
                    ["`" + n + "`" for n in person.keys()]) + ") VALUES (" + ",".join(
                    ["%s" for s in person.keys()]) + ");"

                dbExecute(query, tuple(list(person.values())))
                content = requests.get(person["webLink"], headers={"User-Agent": "XY"}).content
                soup = BeautifulSoup(content, 'html.parser')
                movies = soup.find_all("div",attrs={"class": "card-header card-header-image"})

                for i in movies:
                    href = i.find("a").get("href")
                    movie = {
                        "webLink": params["url"] + href,
                        "endDate": None,
                        "Location": params["code"]
                    }

                    cls.saveMovieToDb(movie, params["code"])

            else:
                movie = json.loads(person["Movies"])[0]
                if movie not in json.loads(selection[0][2]):
                    person["Movies"] = json.loads(selection[0][2])
                    person["Movies"].append(movie)
                    dbExecute("Update Persons set Movies = %s where webLink = %s and Location = %s", (json.dumps(person["Movies"]), person["webLink"], params["code"]))
                print(person)
        except:
            pass


sys.setrecursionlimit(10000)
#: Sample
Loader.getMoviesWillDelete("tr")
