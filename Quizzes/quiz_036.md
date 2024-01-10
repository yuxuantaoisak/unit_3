## Solution ##

```.py

class Converter:
    def __init__(self):
        self.roman_digits = {100: 'C', 90: 'XC', 50: 'L', 10: 'X', 5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1: 'I'}

    def convert2roman(self, decimal: int) -> str:
        if 0 < decimal < 101:
            output = ""
            for k, v in self.roman_digits.items():
                q = decimal // k
                output += v * q
                decimal = decimal % k
        return output


converter_instance = Converter()
print(converter_instance.convert2roman(decimal=11))


```


## Proof of work ##

<img width="1470" alt="Screenshot 2024-01-10 at 20 06 31" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/94d4b19b-27e2-4ba8-99c7-59d37f79bfde">


