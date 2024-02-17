# 1, Create the UML diagram

# 2, Create the SQL series to find the responsible for the fraudulent transaction

## Solution


```.sql


SELECT
    dep.account_id,
    COALESCE(dep.deposit_amount, 0) - COALESCE(w.withdraw_amount, 0) AS net_amount,
    a.balance,
    a.account_type,
    trans.date
FROM
    (SELECT
         account_id, SUM(amount) AS deposit_amount
     FROM
         transactions
     WHERE
         transaction_type = 'deposit'
     GROUP BY
         account_id) AS dep
LEFT JOIN

    (SELECT
         account_id, SUM(amount) AS withdraw_amount
     FROM
         transactions
     WHERE
         transaction_type = 'withdraw'
     GROUP BY
         account_id) AS w ON dep.account_id = w.account_id
LEFT JOIN
    accounts AS a ON dep.account_id = a.account_id
LEFT JOIN
    transactions AS trans ON dep.account_id = trans.account_id

WHERE
    COALESCE(dep.deposit_amount, 0) - COALESCE(w.withdraw_amount, 0) != a.balance and a.balance > net_amount;




```

## Proof of work

<img width="1470" alt="Screenshot 2024-02-17 at 20 24 01" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/428b7744-94c0-4c83-b4fe-8959cd57f9f5">


# 3, What is the name of the customer and the problem that resulted in the bankruptcy of the bank?


## Solution 


```.sql

SELECT * FROM customers WHERE customer_id = 12;

```


## Proof of work

<img width="1470" alt="Screenshot 2024-02-17 at 20 24 52" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/44b1558f-11be-4ec0-8ff6-95e4ef465fd6">


