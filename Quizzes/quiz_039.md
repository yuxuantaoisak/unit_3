## Solution ##

```.py

from kivymd.app import MDApp


class quiz_039(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return

    def button_pressed(self):
        the_label = self.root.ids.label
        the_label.text = f"Count {self.count}"
        self.count += 1


test = quiz_039()
test.run()


```


```.kv


Screen:
    size: 500, 700

    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size_hint: .7, .3


        MDLabel:
            id: label
            md_bg_color: "#add8e6"
            text: "Count"
            halign: "center"
            font_size: "34pt"
            size_hint: .5, 1


        MDRaisedButton:
            id: color
            text: "Add +1"
            font_size: "34pt"
            md_bg_color: "blue"
            pos_hint: {"center_x":0.5, "center_y":0.5}
            size_hint: .5, 1
            on_press:
                app.button_pressed()


```


## Proof of work ##

![Screenshot 2024-01-25 at 23 41 56](https://github.com/yuxuantaoisak/unit_3/assets/144768397/cd8e1adf-08be-41cf-bce2-fb482fac5a62)



## UML diagram ##

<img width="565" alt="Screenshot 2024-01-29 at 18 17 31" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/14c6dca3-7506-47aa-a499-881559cc4b77">
