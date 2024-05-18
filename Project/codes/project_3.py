from typing import Union
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker, MDColorPicker
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
import matplotlib.pyplot as plt
from my_library import DatabaseBridge, get_hash, check_hash


class LoginPage(MDScreen):
    admin = False

    def change_page(self):
        self.parent.current = "SignupPage"

    def show_password(self):
        password_field = self.ids.password
        if password_field.password:
            password_field.password = False
            password_field.helper_text_mode = 'persistent'
        else:
            password_field.password = True
            password_field.helper_text_mode = 'on_focus'

    def try_login(self):
        uname = self.ids.uname.text
        upass = self.ids.password.text
        query = f"""SELECT * FROM users WHERE username = '{uname}'"""
        query_2 = f"""SELECT admin FROM users WHERE username = '{uname}'"""
        db = DatabaseBridge("project_3.db")
        result = db.search(query=query, multiple=True)
        admin = db.search(query=query_2, multiple=True)
        if not result:
            print("Login Unsuccessful")
            self.ids.password.helper_text = "Check your password"
            self.ids.uname.helper_text = "Make sure you've signed up"
            return False
        new_id, new_uname, new_email, hashed, new_admin = result[0]
        if len(result) == 1 and admin == [(0,)] and check_hash(hashed, upass):
            print("Login Successful")
            dialog = MDDialog(title="Logged in", text=f"{uname}, you successfully logged in!")
            dialog.open()
            self.parent.current = "HomePage"
        elif len(result) == 1 and admin == [(1,)] and check_hash(hashed, upass):
            print("Login Successful")
            dialog = MDDialog(title="Logged in", text=f"{uname}, you successfully logged in as an admin!")
            dialog.open()
            self.parent.current = "AdminHome"
            LoginPage.admin = True
        else:
            print("Login Unsuccessful")
            self.ids.password.helper_text = "Check your password"
            self.ids.uname.helper_text = "Make sure you've signed up"


class SignupPage(MDScreen):
    def try_signup(self):
        upass = self.ids.password.text
        cpass = self.ids.password_confirm.text
        email = self.ids.email.text
        if "@" not in email:
            print("Email must include @")
            self.ids.email.helper_text = "Email must include @"
            return
        if upass != cpass:
            print("Passwords do not match")
            self.ids.password.error = True
            self.ids.password_confirm.error = True
            self.ids.password_confirm.helper_text = "Passwords do not match"
            return
        #  the passwords match
        #  check the password policy, length
        if len(upass) < 6:
            print("Password must be at least 6 characters")
            self.ids.password.error = True
            self.ids.password_confirm.error = True
            self.ids.password_confirm.helper_text = "Password must be at least 6 characters"
            return
        elif not any(char.isdigit() for char in upass):
            print("Password must contain one number")
            self.ids.password.error = True
            self.ids.password_confirm.error = True
            self.ids.password_confirm.helper_text = "Password must contain one number"
            return
        elif not any(char.isupper() for char in upass):
            print("Password must contain an uppercase letter")
            self.ids.password.error = True
            self.ids.password_confirm.error = True
            self.ids.password_confirm.helper_text = "Password must contain an uppercase letter"
            return

        email = self.ids.email.text
        username = self.ids.uname.text
        db = DatabaseBridge("project_3.db")
        query = f"""SELECT count(*) from users where email = '{email}'"""
        query_2 = f"""SELECT count(*) from users where username = '{username}'"""
        count = db.search(query, multiple=False)
        count_2 = db.search(query_2, multiple=False)

        if count != (0,):
            self.ids.email.error = True
            self.ids.email.helper_text = "User with that email already signed up"
            return

        elif count_2 != (0,):
            self.ids.uname.error = True
            self.ids.uname.helper_text = "This username has been used"
            return

        try:
            new_user = f"""INSERT INTO users (username, email, password, admin) 
            values ('{username}', '{email}', '{get_hash(upass)}', '{0}')"""
            db.insert(query=new_user)
        except:
            print("An error occurred. Call the customer center.")

        db.close()

        dialog = MDDialog(title="Signed up", text=f"{username}, you successfully signed up!")
        dialog.open()

        self.parent.current = "LoginPage"

    def show_password(self):
        pswd_field = self.ids.password
        pswd_con_field = self.ids.password_confirm
        if pswd_field.password:
            pswd_field.password = False
            pswd_con_field.password = False
            pswd_field.helper_text_mode = 'persistent'
            pswd_con_field.helper_text_mode = 'persistent'
        else:
            pswd_field.password = True
            pswd_con_field.password = True
            pswd_field.helper_text_mode = 'on_focus'
            pswd_con_field.helper_text_mode = 'on_focus'

    def change_page(self):
        self.parent.current = "LoginPage"

    def admin_signup(self):
        self.parent.current = "AdminSignup"


class AdminSignup(MDScreen):
    def try_signup(self):
        username = self.ids.uname.text
        email = self.ids.email.text
        password = self.ids.password.text
        admin_pass = self.ids.admin_password.text
        if "@" not in email:
            print("Email must include @")
            self.ids.email.helper_text = "Email must include @"
            return
        elif not any(char.isdigit() for char in password):
            print("Password must contain one number")
            self.ids.password.error = True
            self.ids.password.helper_text = "Password must contain one number"
            return
        elif not any(char.isupper() for char in password):
            print("Password must contain an uppercase letter")
            self.ids.password.error = True
            self.ids.password.helper_text = "Password must contain an uppercase letter"
            return
        if len(password) < 6:
            print("Password must be at least 6 characters")
            self.ids.password.error = True
            self.ids.password.helper_text = "Password must be at least 6 characters"
            return
        if admin_pass != "123456":
            print("Access denied")
            self.ids.admin_password.error = True
            self.ids.admin_password.helper_text = "Access denied"
            return

        db = DatabaseBridge("project_3.db")
        query = f"""SELECT count(*) from users where email = '{email}'"""
        query_2 = f"""SELECT count(*) from users where username = '{username}'"""
        count = db.search(query, multiple=False)
        count_2 = db.search(query_2, multiple=False)
        if count != (0,):
            self.ids.email.error = True
            self.ids.email.helper_text = "User with that email already signed up"
            return

        elif count_2 != (0,):
            self.ids.uname.error = True
            self.ids.uname.helper_text = "This username has been used"
            return
        try:
            new_user = f"""INSERT INTO users (username, email, password, admin) 
            values ('{username}', '{email}', '{get_hash(password)}', '{1}')"""
            db.insert(query=new_user)
        except:
            print("An error occurred. Call the customer center.")

        db.close()

        dialog = MDDialog(title="Signed up", text=f"{username}, you successfully signed up as an admin!")
        dialog.open()

        self.parent.current = "LoginPage"

    def show_password(self):
        pswd_field = self.ids.password
        pswd_admin_field = self.ids.admin_password
        if pswd_field.password:
            pswd_field.password = False
            pswd_admin_field.password = False
            pswd_field.helper_text_mode = 'persistent'
            pswd_admin_field.helper_text_mode = 'persistent'
        else:
            pswd_field.password = True
            pswd_admin_field.password = True
            pswd_field.helper_text_mode = 'on_focus'
            pswd_admin_field.helper_text_mode = 'on_focus'

    def change_page(self):
        self.parent.current = "LoginPage"


class HomePage(MDScreen):
    def try_logout(self):
        self.dialog = MDDialog(title="Log out", text="Are you sure you want to log out?")
        button_layout = MDBoxLayout(orientation="horizontal")
        yes_button = MDFlatButton(text="Yes", on_press=self.user_logout)
        no_button = MDFlatButton(text="No", on_press=self.cancel_logout)
        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)
        self.dialog.add_widget(button_layout)
        self.dialog.open()

    def user_logout(self, instance):
        if hasattr(self, 'dialog'):
            self.parent.current = "LoginPage"
        self.dialog.dismiss()

    def cancel_logout(self, instance):
        if hasattr(self, 'dialog'):
            self.dialog.dismiss()


class OrderPage(MDScreen):
    def change_page(self):
        if LoginPage.admin is True:
            self.parent.current = "AdminHome"
        else:
            self.parent.current = "HomePage"


class AddOrder(MDScreen):
    def get_items(self, button):
        self.conn = DatabaseBridge("project_3.db")
        query_item = "SELECT DISTINCT items.item_name FROM items"
        self.items = self.conn.search(query=query_item, multiple=True)
        self.menu_items = []
        for i in self.items:
            name = i[0]
            self.menu_items.append(name)
        print(self.menu_items)

        buttons_menu = []

        for name in self.menu_items:
            btn_dict = {"text": str(name),
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=name: self.button_pressed(x)}
            buttons_menu.append(btn_dict)

        self.menu = MDDropdownMenu(caller=button, items=buttons_menu,
                                   width_mult=4)
        self.menu.open()

    def button_pressed(self, name):
        items = self.conn.search(f"SELECT * from items WHERE item_name = '{name}'", False)
        name = items[1]
        self.ids.item_purchased.text = name
        self.menu.dismiss()

    def save(self):
        db = DatabaseBridge("project_3.db")
        customer_name = self.ids.customer_name.text
        items_purchased = self.ids.item_purchased.text
        address = self.ids.address.text
        time_purchased = self.ids.time_purchased.text

        query_amount = f"""SELECT * FROM items WHERE item_name = '{items_purchased}'"""
        result = db.search(query=query_amount, multiple=False)
        amount = int(result[2])

        hashed = get_hash(f"customer {customer_name}, item {items_purchased}, amount {amount}, "
                          f"address {address}, time {time_purchased}")
        query_order = f"""INSERT INTO orders (customer_name, items_purchased, amount, address, time_purchased, signature)
                        VALUES('{customer_name}', '{items_purchased}', {amount}, 
                        '{address}', '{time_purchased}', '{hashed}')
        """

        query_item = f"""UPDATE items SET quantity = quantity - 1 WHERE item_name = '{items_purchased}'"""

        db.run_query(query=query_order)
        db.run_query(query=query_item)
        dialog = MDDialog(title="Order added", text="You successfully added an order!")
        dialog.open()

    def choose_date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.selected_date = value
        value = value.strftime("%m/%d/%Y")
        self.ids.time_purchased.text = f"{value}"


class CheckOrder(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_table = None
        self.selected_row = []

    def on_pre_enter(self, *args):
        column_names = [('id', 40), ('customer_name', 30),
                        ('items_purchased', 80), ('amount', 40),
                        ('address', 50), ('time_purchased', 40), ('signature', 120)]
        self.data_table = MDDataTable(
            size_hint=(.4, .5),
            pos_hint={'center_x': .5, 'top': .8},
            use_pagination=True,
            check=True,
            background_color_header='#689ebd',
            background_color_cell='#689ebd',
            column_data=column_names
        )
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_table)
        self.update()

    def update(self):
        conn = DatabaseBridge("project_3.db")
        data = conn.search(query="SELECT * FROM orders", multiple=True)
        self.data_table.update_row_data(None, data)

    def row_pressed(self, table, cell):
        print(f"cell text{cell.text}")

    def checkbox_pressed(self, table, row_list):
        print(f"row list{row_list}")

    def delete(self):
        checked_rows = self.data_table.get_row_checks()
        print(checked_rows)
        if not checked_rows:
            dialog = MDDialog(title="Empty selection", text="Please select a row!")
            dialog.open()
        else:
            conn = DatabaseBridge("project_3.db")
            for i in checked_rows:
                select_order_id = i[0]
                print(select_order_id)
                query = f"""DELETE FROM orders WHERE id = {select_order_id}"""
                conn.run_query(query=query)
            dialog = MDDialog(title="Order deleted", text="You successfully deleted the order!")
            dialog.open()
            self.update()


class CheckItemsPage(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_table = None
        self.selected_row = []

    def on_pre_enter(self, *args):
        db = DatabaseBridge("project_3.db")

        query_neck_warmer = f"""SELECT quantity FROM items WHERE id = 1"""
        self.neck_warmer = list(db.search(query=query_neck_warmer, multiple=False))
        self.ids.neck_warmer.text = f"Quantity: {str(self.neck_warmer[0])}"

        query_snowboard = f"""SELECT quantity FROM items WHERE id = 2"""
        self.snowboard = list(db.search(query=query_snowboard, multiple=False))
        self.ids.snowboard.text = f"Quantity: {str(self.snowboard[0])}"

        query_boots = f"""SELECT quantity FROM items WHERE id = 3"""
        self.boots = list(db.search(query=query_boots, multiple=False))
        self.ids.boots.text = f"Quantity: {str(self.boots[0])}"

        query_helmet = f"""SELECT quantity FROM items WHERE id = 4"""
        self.helmet = list(db.search(query=query_helmet, multiple=False))
        self.ids.helmet.text = f"Quantity: {str(self.helmet[0])}"

        query_jacket = f"""SELECT quantity FROM items WHERE id = 5"""
        self.jacket = list(db.search(query=query_jacket, multiple=False))
        self.ids.jacket.text = f"Quantity: {str(self.jacket[0])}"

    def update_neck_warmer(self):
        self.ids.neck_warmer.text = f"Quantity: {self.neck_warmer[0]}"
        db = DatabaseBridge("project_3.db")
        query = f"""UPDATE items SET quantity = quantity + 1 WHERE id = 1"""
        db.run_query(query=query)
        db.close()

    def update_snowboard(self):
        self.ids.snowboard.text = f"Quantity: {self.snowboard[0]}"
        db = DatabaseBridge("project_3.db")
        query = f"""UPDATE items SET quantity = quantity + 1 WHERE id = 2"""
        db.run_query(query=query)

    def update_boots(self):
        self.ids.boots.text = f"Quantity: {self.boots[0]}"
        db = DatabaseBridge("project_3.db")
        query = f"""UPDATE items SET quantity = quantity + 1 WHERE id = 3"""
        db.run_query(query=query)
        db.close()

    def update_helmet(self):
        self.ids.helmet.text = f"Quantity: {self.helmet[0]}"
        db = DatabaseBridge("project_3.db")
        query = f"""UPDATE items SET quantity = quantity + 1 WHERE id = 4"""
        db.run_query(query=query)
        db.close()

    def update_jacket(self):
        self.ids.jacket.text = f"Quantity: {self.jacket[0]}"
        db = DatabaseBridge("project_3.db")
        query = f"""UPDATE items SET quantity = quantity + 1 WHERE id = 5"""
        db.run_query(query=query)
        db.close()

    def add_neck_warmer(self):
        self.neck_warmer[0] += 1
        self.update_neck_warmer()

    def add_snowboard(self):
        self.snowboard[0] += 1
        self.update_snowboard()

    def add_boots(self):
        self.boots[0] += 1
        self.update_boots()

    def add_helmet(self):
        self.helmet[0] += 1
        self.update_helmet()

    def add_jacket(self):
        self.jacket[0] += 1
        self.update_jacket()

    def change_page(self):
        OrderPage.change_page(self)


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class CustomizePage(MDScreen):
    def open_color_picker(self):
        color_picker = MDColorPicker(size_hint=(0.45, 0.85))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    def update_color(self, color: list) -> None:
        self.ids.toolbar.md_bg_color = color

    def get_selected_color(
            self,
            instance_color_picker: MDColorPicker,
            type_color: str,
            selected_color: Union[list, str],
    ):

        print(f"Selected color is {selected_color}")
        self.update_color(selected_color[:-1] + [1])

    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        pass

    def choose_model(self):
        diaglog = MDDialog(
            title="Select board Model",
            type="confirmation",
            items=[
                ItemConfirm(text="LumberJack"),
                ItemConfirm(text="Darkside"),
                ItemConfirm(text="Archaic")
            ],
            buttons=[
                MDFlatButton(text="OK"),
                MDFlatButton(text="Cancel"),
            ]
        )
        diaglog.open()

    def cancel(self):
        if hasattr(self, 'dialog'):
            self.dialog.dismiss()

    def save(self):
        dialog = MDDialog(title="Saved", text="You successfully saved your customized snowboard!")
        dialog.open()

    def change_page(self):
        OrderPage.change_page(self)


class AdminHome(MDScreen):
    def try_logout(self):
        HomePage.try_logout(self)

    def user_logout(self, instance):
        HomePage.user_logout(self, instance)

    def cancel_logout(self, instance):
        HomePage.cancel_logout(self, instance)

    def profit_graph(self):
        db = DatabaseBridge("project_3.db")
        profit = []
        date = []
        query = f"""SELECT items.item_name, orders.items_purchased, items.profit, time_purchased
                    FROM orders
                    INNER JOIN items on item_name = items_purchased
                    """
        x = db.search(query=query, multiple=True)
        print(x)
        for i in x:
            profit.append(i[2])
            date.append(i[3])

        plt.plot(date, profit, label="Profit Graph by Date")
        plt.xlabel("Date")
        plt.ylabel("Daily profit in ¥")
        plt.xticks(rotation=45)
        plt.show()


class project_3(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        Window.size = (900, 900)


test = project_3()
test.run()
