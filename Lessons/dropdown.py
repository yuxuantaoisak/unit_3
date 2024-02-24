from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from my_library import DatabaseBridge


class demoDropDown(MDApp):
    def build(self):
        self.x = DatabaseBridge('bitcoin_exchange.db')
        query_customer = "SELECT * FROM users"
        self.customers = self.x.search(query_customer, multiple=True)
        Window.size = (500, 700)

    def get_customers(self, button):
        self.menu_items = []
        for c in self.customers:
            name = c[1]
            self.menu_items.append(name)

        buttons_menu = []
        for name in self.menu_items:
            btn_dict = {"text": name,
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=name: self.button_pressed(x)}
            buttons_menu.append(btn_dict)

        self.menu = MDDropdownMenu(caller=button, items=buttons_menu,
                                   width_mult=2)
        self.menu.open()

    def button_pressed(self, name):
        customer = self.x.search(f"SELECT * from users WHERE name='{name}'", False)
        id = customer[0]
        name = customer[1]
        self.root.ids.results.text = f"Customer: {name} with id {id}"
        self.root.ids.add_user.text = name
        self.menu.dismiss()


test = demoDropDown()
test.run()
test.x.close()

