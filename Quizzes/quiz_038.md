## Solution ##


```.py

import random
import matplotlib.pyplot as plt


class SalesmanMap:

    def __init__(self):
        self.name = None
        self.x = []
        self.y = []

    def set_names(self, names_2):
        self.name = names_2

    def get_map(self):

        for i in range(len(self.name)):
            self.x.append(random.randint(1, 100))
            self.y.append(random.randint(1, 100))

        plt.scatter(self.x, self.y)
        plt.xlabel("Distance (km)")
        plt.ylabel("Distance (km)")

        for i, name in enumerate(self.name):
            plt.text(self.x[i], self.y[i], name, fontsize=9)

        plt.show()


c = SalesmanMap()
c.set_names(['Kobe', 'Gifu', 'Kawasaki', 'Osaka', 'Kyoto', 'Tokyo', 'Sapporo', 'Chiba', 'Karuizawa', 'Nagano'])
c.get_map()


```


## Proof of work ##

<img width="1366" alt="Screenshot 2024-01-29 at 15 25 56" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/0ddb0ded-72b8-42c0-a97e-f4a448ecc56c">



## UML diagram ##

| Class: SalesmanMap             |
|--------------------------------|
| self.name = None               |
|self.x = []                     |
|self.y = []                     |
|--------------------------------|
|set_names(self, names_2)        |   
|get_map(self)                   |
