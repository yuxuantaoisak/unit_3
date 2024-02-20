## Solution

```.py

class Quiz050:
    def __init__(self, flight_num: str, origin: str, destination: str, departure_time: str, duration: list):
        self.flight_num = flight_num
        self.origin = origin
        self.departure_time = departure_time
        self.destination = destination
        self.duration = duration

    def get_duration(self):
        h = self.duration[0]
        m = self.duration[1]
        s = self.duration[2]
        dest = self.destination
        return f"{h} hours {m} minutes {s} remaining for {dest}"


obj_1 = Quiz050(flight_num="AA123", origin="London",
                destination="Paris", departure_time="11:00AM", duration=[2, 40, 20])
obj_2 = Quiz050(flight_num="BD742", origin="Beijing",
                destination="Shanghai", departure_time="8:00PM", duration=[4, 10, 6])

print(obj_1.get_duration())
print(obj_2.get_duration())

```
## Proof of work

<img width="1470" alt="Screenshot 2024-02-20 at 18 12 07" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/ad0e50cb-c3a1-44c9-88ba-a6e317bb33e0">

