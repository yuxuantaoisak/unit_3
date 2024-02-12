# 1, How many tables are there in the database?


## Solution 


## Proof of work


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

<img width="662" alt="Screenshot 2024-02-13 at 0 01 00" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/00ce4a12-123b-4752-bcba-1364b7827f04">


# 4, How many items are there that start with the letter "A"?


## Solution 


## Proof of work

# 5, How many different jobs are there?


## Solution 


## Proof of work


# 6, What are the items owned by the herbalists?



## Solution 


## Proof of work
