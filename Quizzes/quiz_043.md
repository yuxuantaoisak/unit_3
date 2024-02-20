# 1, How many tables are there in the database?


## Solution 

4


## Proof of work

<img width="300" alt="Screenshot 2024-02-13 at 16 22 36" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/ce1f3bdb-100c-4249-bca2-1ee8b149b004">


# 2, How many Male inhabitants are Friendly?



## Solution 

```.sql

SELECT * FROM INHABITANT WHERE gender = 'Male' AND state = 'Friendly';

```

## Proof of work


<img width="952" alt="Screenshot 2024-02-12 at 23 57 10" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/b38574aa-8f98-4d82-82e8-55ecc2980682">


# 3, What is the average gold by village?


## Solution 

```.sql

SELECT villageid, AVG(gold) from INHABITANT group by villageid;

```

## Proof of work

<img width="1470" alt="Screenshot 2024-02-13 at 16 19 44" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/b5bf8c61-44c0-4f65-ae35-7b7ff4133442">


# 4, How many items are there that start with the letter "A"?


## Solution 

```.sql

SELECT * from ITEM WHERE item LIKE 'A%';

```

## Proof of work


<img width="1470" alt="Screenshot 2024-02-13 at 16 19 13" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/713c8bbb-b24a-47ca-a7b8-85271331fa36">


# 5, How many different jobs are there?


## Solution 

```.sql

SELECT distinct job from INHABITANT;

```

## Proof of work

<img width="1470" alt="Screenshot 2024-02-13 at 15 38 50" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/2df036d7-8362-4a54-8bf5-0d0294f2e218">


# 6, What are the items owned by the herbalists?


## Solution 



```.sql

SELECT ITEM.item, INHABITANT.personid
from INHABITANT
INNER JOIN ITEM on ITEM.owner = INHABITANT.personid
WHERE INHABITANT.job = 'Herbalist';

```

## Proof of work


<img width="1470" alt="Screenshot 2024-02-13 at 16 18 45" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/ad261c5a-055e-435b-962b-eac9e01cc14d">


# ER diagram

<img width="1303" alt="Screenshot 2024-02-20 at 23 05 13" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/0bd97d60-9576-42f1-95fa-a5dd0d8560b4">
