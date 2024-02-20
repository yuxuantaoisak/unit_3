## Solution

```.py

class Quiz050:
    def __init__(self, flight_num: str, origin: str, destination: str, departure_time: str, duration: list[int]):
        self.flight_num = flight_num
        self.origin = origin
        self.departure_time = departure_time
        self.destination = destination
        self.duration = duration

    def get_duration(self):
        h = self.duration[0]
        m = self.duration[1]
        s = self.duration[2]
        return f"{h} hours {m} minutes {s} seconds"


obj_1 = Quiz050(flight_num="AA123", origin="London",
                destination="Paris", departure_time="11:00AM", duration=[2, 40, 20])
obj_2 = Quiz050(flight_num="BD742", origin="Beijing",
                destination="Shanghai", departure_time="8:00PM", duration=[4, 10, 6])


text = (f"This is flight number {obj_1.flight_num}, flying from {obj_1.origin} to {obj_1.destination}. "
        f"This journey takes {obj_1.get_duration()}")
text_2 = (f"This is flight number {obj_2.flight_num}, flying from {obj_2.origin} to {obj_2.destination}. "
        f"This journey takes {obj_2.get_duration()}")

print(text)
print(text_2)


```
## Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 23 37 58" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/8a4975e4-2043-440f-bc87-3723e010d5ee">


## UML diagram

<img width="484" alt="Screenshot 2024-02-20 at 20 07 28" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/e02bcbe2-65a7-420c-b0ea-bc04b3057574">
