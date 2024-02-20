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
print(f"Total valid transactions: {total}")

```

## Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 17 56 19" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/02934664-0b6a-4eb5-883f-154925a1ec46">
