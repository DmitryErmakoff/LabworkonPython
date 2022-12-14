import datetime
import json

from pathlib import Path

path_p = Path("jsons", "c.json")
path_m = Path("jsons", "d.json")
path_ex = Path("jsons", "ex.json")
path_ex2 = Path("jsons", "ex2.json")

class Printing:
    def __init__(self):
        self.__name = "Alenvic" 
        self.__year = 5

    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)



class Magazine(Printing):
    def __init__(self):
        super().__init__()
        self.__date = datetime.datetime(2000, 1, 1)


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__date = datetime.datetime(
                obj["date"]["year"],
                obj["date"]["month"],
                obj["date"]["day"]
            )


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year,
            "date": {
                "year":  self.__date.year,
                "month": self.__date.month,
                "day":   self.__date.day
            }
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)


class Book(Printing):
    def __init__(self):
        super().__init__()
        self.__genre = "genre"


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__genre = obj["genre"]


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year,
            "genre": self.__genre
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)


class Schoolbook(Book):
    def __init__(self):
        super().__init__()
        self.__subject = "subject"


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__genre = obj["genre"]
            self.__subject = obj["subject"]


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year,
            "genre": self.__genre,
            "subject": self.__subject
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)

p = Printing()
p.json_load("ex.json")
p.json_save("p.json")

m = Magazine()
m.json_load("ex2.json")
m.json_save("m.json")




