# FlixWatcher
This code repository allows you to pull information about Netflix movies and actors from a particular site, and the last watch date of movies that will be removed from Netflix.

## Installation

**Be sure to use the same version of the code as the version of the docs you're reading.**
You probably want the latest tagged version, but the default Git version is the master branch.

```shell
# clone the repository
$ git clone https://github.com/furkankyildirim/FlixWatcher
$ cd FlixWatcher
# checkout the correct version
$ git tag
```

Create a virtualenv and activate it:
```shell
$ python3 -m venv venv --without-pip
$ source venv/bin/activate
```

Install pip3 requirements
```shell
$ pip3 install -r requirements.txt
```

## Run
```shell
$ source venv/bin/activate
$ python3 main.py
```

When the program starts, it reflects the player and movie data taken from the website to the console. It also saves movie and player data to the database you specify in the config.ini file.

## Edit Config File

Edit the [config.ini](https://github.com/furkankyildirim/FlixWatcher/tree/master/config.ini) file so that the program can run on your own computer.
```text
[Database]
host = Your_hostname
user = Your_username
pass = Your_password
db = Your_DBname
```