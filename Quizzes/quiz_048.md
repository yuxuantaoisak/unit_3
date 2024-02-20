## Solution

```.py

from my_library import DatabaseBridge, check_hash

db = DatabaseBridge("bitcoin_exchange.db")

query = "SELECT * FROM ledger"
result = db.search(query=query, multiple=True)
print(result)
db.close()
total = 0
for row in result:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    signature = row[4]
    text = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if check_hash(signature, text):
        total += amount
print(f"Total valid transaction amount: {total}")

```

## Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 23 43 55" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/0326772a-0aa2-43b9-931d-2d7524020906">

## ER diagram

<img width="747" alt="Screenshot 2024-02-20 at 22 38 32" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/86bbc8f4-d034-4d3b-9e04-8360f0b0e739">

