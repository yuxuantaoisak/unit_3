## Solution

```.py

# need to update

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



## Create a query to get all the transactions involving user id 920

### Solution

```.sql

SELECT * FROM ledger join user on ledger.receiver_id = user.id WHERE user.name = 'Adam';

```

### Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 20 45 01" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/0ebdf46c-ce12-47da-8587-9439a15ad877">
