import sqlite3
from passlib.hash import sha256_crypt

hash_function = sha256_crypt.using(rounds=30000)


def get_hash(text: str):
    return hash_function.hash(text)


def check_hash(input_hash, text):
    return hash_function.verify(text, input_hash)


class DatabaseBridge:
    def __init__(self, name):
        self.db_name = name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()

    def create(self):
        #anything we need to do at the moment of creating the db
        print("[DatabaseBridge]Creating the Database")
        query = """CREATE TABLE if not exists users (
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(100) not null unique,
                    email varchar(100) not null unique,
                    password varchar(256) not null
                )
                """

    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connect.commit()

    def insert(self, query: str):
        print("[DatabaseBridge]Inserting into db")
        self.run_query(query=query)

    def search(self, query, multiple: False):
        #this method runs a query in the db
        #query: the sql command
        #if true: returns multiple rows
        #return a list [] or a list of lists[[], [], []]
        results = self.cursor.execute(query)
        if multiple == True:
            return results.fetchall()
        return results.fetchone()
