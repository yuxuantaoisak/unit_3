## Solution ##

```.py

import sqlite3


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
        self.run_query(query=insert_query)

    def search(self, query, multiple: False):
        #this method runs a query in the db
        #query: the sql command
        #if true: returns multiple rows
        #return a list [] or a list of lists[[], [], []]
        results = self.cursor.execute(query)
        if multiple == True:
            return results.fetchall()
        return results.fetchone()


haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves"""


my_db = DatabaseBridge('quiz_045.db')
create_query = """CREATE TABLE if not exists WORDS(
    id INTEGER PRIMARY KEY,
    length int,
    word text
)
"""

my_db.run_query(query=create_query)


for word in haiku.split():
    insert_query = f"""INSERT INTO WORDS (length, word)
    values({len(word)}, '{word}')"""
    my_db.run_query(query=insert_query)


q = "SELECT avg(length) from WORDS"
out = my_db.search(query=q, multiple=False)
my_db.close()
print("Average word length is", out)




```



## Proof of work ##

<img width="1470" alt="Screenshot 2024-02-17 at 20 31 48" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/624d5dfd-22aa-4bb1-85a3-9ff702831753">


