## Solution

```.py

from my_library import DatabaseBridge

db = DatabaseBridge("bitcoin_exchange.db")

table = """CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY
user_id INT
name TEXT NOT NULL
email TEXT NOT NULL"""

db.run_query(table)

user_info = """INSERT INTO user (user_id, name, email) VALUES (560, 'John', 'john@xyz.com'),
(371, 'Smith', 'smith@xyz.com'), (488, 'Alice', 'alice@xyz')"""

db.run_query(user_info)



```



## Proof of work
