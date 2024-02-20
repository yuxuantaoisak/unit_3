## Solution

```.py


from my_library import DatabaseBridge

db = DatabaseBridge("bitcoin_exchange.db")

table = """CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL)"""

db.run_query(table)

user_info = """INSERT OR IGNORE INTO user (id, name, email) VALUES (560, 'John', 'john@xyz.com'),
(371, 'Smith', 'smith@xyz.com'), (488, 'Alice', 'alice@xyz'), (561, 'Ani', 'ani@xyz.com'),
(254, 'Val', 'val@xyz.com'), (920, 'Adam', 'adam@xyz.com'), (438, 'Ana', 'ana@xyz.com'),
(744, 'Niko', 'niko@xyz.com'), (261, 'Sayaka', 'sayaka@xyz')"""

db.run_query(user_info)

```


## Proof of work


<img width="1470" alt="Screenshot 2024-02-20 at 20 49 05" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/a500f06e-ba3c-4057-a28b-db0e67c674f8">


## Create ER diagram

<img width="1298" alt="Screenshot 2024-02-20 at 22 35 56" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/28bf0e53-d5a2-4351-8ba2-127f7efa6995">


## Create a query to get all the transactions involving user id 920

### Solution

```.sql

SELECT * FROM ledger join user on ledger.receiver_id = user.id WHERE user.name = 'Adam';

```

### Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 20 45 01" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/0ebdf46c-ce12-47da-8587-9439a15ad877">
