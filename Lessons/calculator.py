from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton


class calculator(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.equation_text = ""

    def build(self):
        pass


class MyButton(MDFlatButton):
    pass


class OrangeButton(MDFlatButton):
    pass


test = calculator()
test.run()
