## Solution ##

```.py


from kivymd.app import MDApp


class quiz_040(MDApp):
    def build(self):
        return

    def button_pressed(self):
        the_color = self.root.ids.label
        the_color.md_bg_color = "black"
        the_color.color = "white"


test = quiz_040()
test.run()


```




```.kv

Screen:
    size: 500, 600

    MDLabel:
        id: label
        text: "yuxuantao"
        halign: "center"
        font_size: "34pt"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size_hint: 1, 1

    MDRaisedButton:
        id: dark_mode
        text: "Dark mode"
        md_bg_color: "blue"
        pos_hint: {"center_x":0.1, "center_y":0.1}
        size_hint: .1, .1
        on_press:
            app.button_pressed()
```



## Proof of work ##

https://github.com/yuxuantaoisak/unit_3/assets/144768397/0c965fae-836a-464f-8d14-680974e4f69f
