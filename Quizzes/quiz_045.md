## Solution ##

```.py

import sqlite3
from my_library import DatabaseBridge

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


## ER diagram

<img width="402" alt="Screenshot 2024-02-20 at 22 42 33" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/b294f6b9-8142-47a8-8693-02771aa1e35b">

