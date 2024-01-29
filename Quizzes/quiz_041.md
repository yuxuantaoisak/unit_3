## Solution ##

```.py


#quiz_041.py



from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.core.window import Window


class Spacer(MDLabel):
    pass


class MyButton(MDFlatButton):
    pass


class quiz_041(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turn = 1

    def build(self):
        Window.size = (500, 500)
        pass

    def toggle_color(self, btn):
        if self.turn % 2 == 1:
            self.root.ids.turn.text = "It is O's turn"
            btn.text = "X"
            self.turn = 0
            btn.md_bg_color = "red"

        else:
            self.root.ids.turn.text = "It is X's turn"
            btn.text = "O"
            self.turn = 1
            btn.md_bg_color = "yellow"


test = quiz_041()
test.run()


```



```.kv

#quiz_041.kv



Screen:

    size: 600, 500

    MDLabel:
        id: tic
        pos_hint: {"center_x":.5, "center_y":.9}
        text: "Tic Tac Toe by Yuxuan Tao"
        font_size: "25pt"
        halign: "center"

    MDLabel:
        id: turn
        pos_hint: {"center_x":.5, "center_y":.8}
        text: "It is X's turn"
        font_size: "25pt"
        halign: "center"

    MDBoxLayout:
        orientation: "vertical"
        size_hint: 1, .7

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .2
            md_bg_color: "white"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .2
            md_bg_color: "green"

            Spacer:
            MyButton:
            MyButton:
            MyButton:
            Spacer:

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .2
            md_bg_color: "green"

            Spacer:
            MyButton:
            MyButton:
            MyButton:
            Spacer:

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .2
            md_bg_color: "green"

            Spacer:
            MyButton:
            MyButton:
            MyButton:
            Spacer:

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .2
            md_bg_color: "white"


<Spacer>:
    md_bg_color: "white"
    size_hint: 1, 1


<MyButton>:
    size_hint_y: 1
    size_hint_x: 1
    md_bg_color: "219ebc"
    on_press:
        app.toggle_color(self)




```


## Proof of work ##



https://github.com/yuxuantaoisak/unit_3/assets/144768397/1e25f3aa-1c1f-4403-b61f-d4e6896cc01e


## UML diagram ##

<img width="878" alt="Screenshot 2024-01-29 at 18 52 47" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/d6ce3835-fca3-4716-86f4-dca1256c9d56">

