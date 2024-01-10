class Tray:
    def __init__(t, mat: str, price: int, cst: int, color: list, mf: str):
        t.material = mat
        t.price = price
        t.cost = cst
        t.color = color
        t.main_function = mf

    #define a method to return the profit
    def get_profit(t) -> int:
        return t.price - t.cost


    def get_color(t):
        return t.color


    def paint(t, new_color: list):
        if len(new_color) == 3 and min(new_color) > -1 and max(new_color) < 256:
            t.color = new_color
        else:
            print("New color is invalid")


tray1 = Tray(mat="plastic", price=100, cst=80, color=[0, 0, 0], mf="print, copy")
tray2 = Tray(mat="wood", price=500, cst=480, color=[0, 0, 0], mf="print")
tray1.paint([125, 0, 0])
print(f"The color of tray1 is {tray1.get_color()}")

