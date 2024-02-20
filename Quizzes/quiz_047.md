## Solution

```.py

from my_library import DatabaseBridge, check_hash

db = DatabaseBridge("bitcoin_exchange.db")

query = """SELECT * FROM ledger"""
results = db.search(query=query, multiple=True)
print(results)
db.close()

for row in results:
    t_id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    signature = row[4]

    text = f"id {t_id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"

    verified = check_hash(signature, text)

    if verified is True:
        print(f"Tx (id={t_id}) Signature matches")
    else:
        print(f"Tx (id={t_id}) Error signature")


```



## Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 17 51 35" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/a99b9110-d353-4a29-bcce-535265425dbd">

## ER diagram

<img width="737" alt="Screenshot 2024-02-20 at 22 40 00" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/845fdc62-c6ee-4d81-8038-92d31f873400">
