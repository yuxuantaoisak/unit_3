## Solution ##

```.py

class CompoundInterest:
    def __init__(self, principal, rate, no_yr):
        self.principal = principal
        self.rate = rate
        self.no_yr = no_yr

    def calculate_interest(self):
        return self.principal * (1 + self.rate) ** self.no_yr


class AccountingProgram(CompoundInterest):
    def __init__(self, principal, rate, no_yr):
        super().__init__(principal, rate, no_yr)

    def interest_calculator(self):
        interest = CompoundInterest.calculate_interest(self)
        return interest


accounting_program = AccountingProgram(principal=1000, rate=0.15, no_yr=10)
test = accounting_program.interest_calculator()
print(test)


```


## Proof of work ##

<img width="1470" alt="Screenshot 2024-01-19 at 21 09 22" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/8cea3bde-83ae-47ab-9af6-dd5abfae2b08">



## UML diagram ##

<img width="284" alt="Screenshot 2024-01-29 at 19 48 37" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/c039a823-bb82-4045-a13c-e349d27fd3e0">


