## Code ##

```.py

def mystery(list_1, list_2):
    output = []
    for i in range(len(list_1)):
        for n in range(len(list_2)):
            if list_1[i] == list_2[n]:
                output.append(list_1[i])

    return output


a = [1, 3, 5, 7, 9]
b = [3, 4, 5, 6]
print(mystery(a, b))


```

## Proof of work ##

<img width="1470" alt="Screenshot 2024-01-09 at 16 18 19" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/06fe9808-a190-4a89-9a15-07b6489dc43b">

