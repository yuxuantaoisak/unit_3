# Unit 3: Online Order Tracker System for a Snowboard Company

![image](https://github.com/yuxuantaoisak/unit_3/assets/144768397/462102b4-c63c-49c3-96c4-1a441f8cebff)
*blogto.com* [1]


# Criteria A: Planning


## Problem Definition


My client is a snowboard factory owner. He is passionate about making various kinds of snowboards for snowboarders of all levels. However, he has recently encountered some problems with the management of his factory. Because of the increase in the number of clients, he is having some difficulties managing the online orders. He tried to write down order details for his employees to send packages everyday, but it does not work anymore with the huge increase in order numbers. Moreover, this triggers a problem: the employees now know all the trade secrets of the company, such as private customer data, revenue of the company, etc. If the problem keeps getting worse, my client faces consequences such as losing customers, losing revenue, losing reputation in the industry, and the customer loyalty that he just built recently. Another problem he is facing right now is that he does not like the design of the current snowboard model. 


## Proposed Solution

Considering the challenges that my client is facing, I will develop a manual program with a GUI(Graphical User Interface) for the client and his employees to track online orders, while providing the manager and employees with different user accesses. The order details with various attributes will be stored in an online database. This centralized user-centered program will be developed using KivyMD, Python, and SQLite. 

The application will have a GUI output instead of a text output in order to meet the client's requirement of organizing the details of online orders into tables. Additionally, with a GUI that represents data in a visually attractive way, my client can understand and manage orders easily. Thus I decided to use GUI as the output. 

Since my client has a MacBook Pro, the application can be developed using either Xcode or Python, as both of them are compatible with a MacBook. I decided to use Python because of its popularity, community support, and a variety of Python libraries[2]. The popularity and the open source feature of Python makes it to make reference to the codes of other developers which can significantly improve the development of the application. Furthermore, the large number of developers using Python makes it an easy-to-understand language. The upcoming programmers will easily understand the code so that they can make further improvements, whereas Xcode is focused on the development of iOS applications so only a small number of programmers are familiar with this language. Thus, Python is an appropriate choice for developing the application. 

Regarding the application interface, I decided to use KivyMD. KivyMD is a Python-based framework for the development of user interfaces. It has various bult-in widgets that can be easily changed and customized[3]. This allows my client to have a better user experience with the application, and order details can be organized in a more user-centered and visually appealing manner. Additionally, KivyMD offers much better consistency than other cross-platform GUI toolkit like PyQT[4]. KivyMD is very unlikely to get crashed or hacked, which allows my client to build customer trust and reputation in the snowboard industry. Thus, KivyMD is adequate for the development of the interface of this application. 

Lastly, I chose SQLite as the database for the application. SQLite is a relational database that allows user to interact with each database. It's free to use so it does not cost any extra for my client. MySQL has the same functionalities as SQLite. However, SQLite is much more lightweight and it's a better fit for developing mobile, small-scale applications[5], which is the kind of application I will develop based on my client's requirements. Moreover, SQLite is a good fit for embedded applications: it requires minimum setup and configuration settings so my client does not need to waste time on setting up his devices. So, SQLite is a better choice for the relational database management system in developing this application over other options such as MySQL or non-SQL databases. 


## Success Criteria


1. The GUI application has a secure login and registration system. [issue tackled: "I want my privacy and the customers' order details to be secured"]
2. The GUI application has different accesses for admin and other users. [issue tackled: ""]
3. The GUI application provides a window to create snowboards where the user can enter attributes including color, material, price, and number. [issue tackled: ""]
4. The GUI application provides a window to create orders where the user can enter attributes including customer's name, items purchased, address, and total amount. [issue tackled: ""]
5. The application provides a money tracker in which the user can check the profit represented by a diagram. [issue tackled: ""]
6. The GUI application provides a window to check revenue represented by a diagram that is exclusively for the admin. [issue tackled: ""]
7. The GUI application provides customization function for the user to change the design of the snowboard according to their likings. [issue tackled: ""]



# Criteria B: Solution Overview

## System diagram

## Wireframe diagram

## ER diagram

## UML diagram

## Flow diagrams

## Test plan

## Record of tasks



# Criteria C: Development


## List of techniques used


| **Software development tools** | **Coding structure tools**           | **Libraries**  |
|--------------------------------|--------------------------------------|----------------|
| Pycharm                        | OOP structure (classes, inheritance) | KivyMD library |
| Relational database            | Objects and attributes               | matplotlib     |
| SQLite                         | For loop                             | datetime       |
| Python                         | If statement                         | my_library.py  |
| KivyMD                         | Elif statement                       |                |
|                                | Try statement                        |                |


## Main file: "project_3.py"

## Importing methods that I need in building the application

```.py

from my_library import DatabaseBridge, get_hash, check_hash

```
I imported two methods and a class: get_hash, check_hash, and DatabaseBridge from a file called "my_library". The DatabaseBridge class helps me connect to the relational database that stores all the data in this project. It allows me to interact with the database through python by running the SQL queries. The two main methods inside the DatabaseBridge class are run_query and search. Run query allows me to run a SQL query through python, while the search method can return the result of the query ran. 

```.py
class DatabaseBridge:
    def __init__(self, name):
        self.db_name = name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def close(self):
        # code omitted

    def create(self):
        # code omitted

    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connect.commit()

    def insert(self, query: str):
        # code omitted 

    def search(self, query, multiple: False):
        results = self.cursor.execute(query)
        if multiple is True:
            return results.fetchall()
        return results.fetchone()

```

The search method above takes a SQL query and "multiple" as the inputs. The method executes the query using a cursor object and fetches result. The default value of the "multiple" parameter is False, meaning that only a single result will be fetched. If it's True, all results will be fetched and returned as output. 



```.py

def get_hash(text: str):
    return hash_function.hash(text)


def check_hash(input_hash, text):
    return hash_function.verify(text, input_hash)

```

Two other methods I imported are get_hash and check_hash. The get_hash method takes a string as the input, and returns another string encrypted by the sha-256 encryption from the passlib library. This method allows me to encrypt user data so that they are safe from hackers and possible information leaks.

The check_hash function takes an encrypted hash and a text as inputs. Using the same sha-256 encryption, it checks if the two inputs correspond. This method helps me with the login system and validation system. 

## Signup Page

As stated in success criteria, my client required a login and registration system that are secured. I designed a class called SignupPage with all the useful methods. 

### try_signup

When a new user tries to sign up, the try_signup function will check all possible mistakes and matches with the user input, as well as enforcing the company's password policy.

```.py

if upass != cpass:
  print("Passwords do not match")
  self.ids.password.error = True
  self.ids.password_confirm.error = True
  self.ids.password_confirm.helper_text = "Passwords do not match"
  return
#the passwords match
#check the password policy, length
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

```

Here, the method first checks if the password the user set and the confirm password match (the user is asked to enter the password twice to confirm). If they do not match, the helper text will remind the user that the two passwords do not match. Then, it checks if the password set by the user has more than 6 characters as part of the company's password policy to ensure safety. Another requirement of the password policy is that the password has to contain at least one number and one upper case letter. I used python's isdigit() and isupper() methods to achieve this. These two methods and build-in for python. They check whether a string contains a digit/upper case letter or not, and return true or false. 


```.py

email = self.ids.email.text #get the email form GUI
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

```

After confirming that the password is acceptable under the password policy, the search method from DatabaseBridge class connects to the relational database and runs the queries that are responsible for finding whether the username and password exist among the current user. The count and count_2 variable stores the result returned. If either of them is not 0, meaning that other existing user(s) has the same username or email, the helper text will remind the user that the username or email has been used already. 

This ensure that users do not share username or password, which will lead to confusion between the users and their accesses to different functions. Unique usernames and emails help my client manage the company's employees better, preventing the possibility of mixing up users or the same user signing up twice. 

```.py

        try:
            new_user = f"""INSERT INTO users (username, email, password, admin) 
            values ('{username}', '{email}', '{get_hash(upass)}', '{0}')"""
            db.insert(query=new_user)

```

After confirming that all requirements are met, the try block was used to insert the information, including username, email, password, and admin status into the database "project_3.db" using the DatabaseBridge class. he password is encrypted by the get_hash method I imported. The admin status is automatically set as 0, or false (the SQLite database does not accept Boolean value, so I had to use 0 and 1 to represent true and false), since this is the signup page for normal users. Then, a pop up window will show that the user has successfully signed up. The window will automatically jumps to login page after that.


## Admin Signup

As part of my client's requirement, the admin user should be provided with extra functions. Thus, I designed a signup window that is exclusively for the admin user. The admin signup page asks for an extra admin password, which validates the user's identity. This password that allows the user to sign up as an admin is set by the owner of the snowboard company. If the user enters the correct admin password, the system can confirm that they are authorized by the owner to sign up as an admin with the access to extra functions. 

```.py

if admin_pass != "123456":
    print("Access denied")
    self.ids.admin_password.error = True
    self.ids.admin_password.helper_text = "Access denied"
    return
```
Above is the code confirming that the admin password is correct. If not, the helper text will tell the user that they are denied access. 

After the system confirms that the admin password is correct, it checks if other requirements are met just like how it does in signup page. 

```.py

try:
    new_user = f"""INSERT INTO users (username, email, password, admin) 
    values ('{username}', '{email}', '{get_hash(password)}', '{1}')"""
    db.insert(query=new_user)

```

This time, the admin status is automatically set as 1, or true, meaning that the user signed up as an admin. 


## Login Page

After the user signs up, they will see login page where they are required to enter username and password. I designed a try_login method for the login function. 

```.py

def try_login(self):
    uname = self.ids.uname.text
    upass = self.ids.password.text
    query = f"""SELECT * FROM users WHERE username = '{uname}'"""
    query_2 = f"""SELECT admin FROM users WHERE username = '{uname}'"""
    db = DatabaseBridge("project_3.db")
    result = db.search(query=query, multiple=True)
    admin = db.search(query=query_2, multiple=True)

```

In this method, the user input of username and password are retrieved from the GUI as two variables, uname and upass. Then, two SQL queries are constructed using the two variables. The DatabaseBridge class object is defined as db, and then its method search is called. Using the search method, the first query returns all attributes of the user, while the second query returns specifically the admin status of the user. 

```.py

new_id, new_uname, new_email, hashed, new_admin = result[0]

```

All the attributes of the returned result are named accordingly. 


```.py

if len(result) == 1 and admin == [(0,)] and check_hash(hashed, upass):
    self.parent.current = "HomePage"

elif len(result) == 1 and admin == [(1,)] and check_hash(hashed, upass):
    self.parent.current = "AdminHome"
    LoginPage.admin = True

else:
    print("Login Unsuccessful")

```

To complete logging in, there are three conditions that all need to be satisfied: the length of the result variable is exactly one, meaning that there are only one user information that corresponds with the information entered by the user; the admin status is either 0, normal user, or 1, admin user; checked_hash must return true.  

Since the password is not directly stored into the database as it appears, the check_hash method must be used to validate the password. It compares a hash and a original text to see if they match, and return true or false. Here, it must return true for the program to proceed. 

As the code shows, if the admin status is 0 (false), the user will jump to home page for normal users, while the page turns to admin home page if admin status is 1 (true). With this design, the user can go to their respective home pages without entering extra information on their admin status, as the system automatically communicates with the SQL database to confirm the user's admin status. 

Also, the LoginPage.admin class variable is defined as True if the user logs in as an admin. This variable can be passed and used in other classes in order to confirm whether the current user is an admin or not, and further display corresponding pages and functions according to their status.  


![Screenshot 2024-03-07 at 0 26 59](https://github.com/yuxuantaoisak/unit_3/assets/144768397/fefa0b9e-a791-47fd-bcb5-18892632b3ba)



_Fig. 1_


**Fig. 1** is a snapshot of the user entity in the database. As shown in the photo, the passwords are encrypted so that they won't get leaked even if people outside the company see this page, making the users' information more secure. Also, the admin status is recorded as either 0 or 1.

### show_password

In both login and signup pages, I defined a method called show_password. 

```.py

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

```


The method takes self as the input. It also retrives the passwords from the GUI and stores them into the variables. If the password is currently visible, the function sets the "password" attribute to False to hide the password and sets the "helper_text_mode" attribute to "persistent" to display a helper message. If the password is currently hidden, the function sets the "password" attribute to True to show the password and sets the "helper_text_mode" attribute to "on_focus" to display the helper message when the field is on focus. 

This function hides the password that the user enters when they login or signup, while the user can still choose to show the password when needed by clicking the checkbox in the GUI, which runs the show_password method when pressed. This ensures that the password is secured so that the important information in this application doesn't leak. 

## Add Order Page

In this page, the user can add an online that is to be mailed. The attributes include customer name, item purchased, amount, address, time, and hash signature. 

### Select item purchased

This is a dropdown menu constructed by the widget MDDropDownItem from the kivymd library. When the user clicks the dropdown menu, a list of products appears, and the user can select which product is included in the order. 

```.py

def get_items(self, button):
    self.conn = DatabaseBridge("project_3.db")
    query_item = "SELECT DISTINCT items.item_name FROM items"
    self.items = self.conn.search(query=query_item, multiple=True)
    self.menu_items = []
    for i in self.items:
        name = i[0]
        self.menu_items.append(name)
    print(self.menu_items)

```

In the get_items class, used the search attribute from the DatabaseBridge class to interact with the database. The method returns the result (all item names) of the SQL query, which is then appended to self.menu_items list. When the user clicks the dropdown button, a menu with all products appears, and the user can choose which product they want to include in the order. 

<img width="365" alt="Screenshot 2024-03-07 at 18 05 01" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/01d22c5e-91c8-4bf1-91ba-273fc6b83489">


_Fig. 2_



**Fig. 2** shows the dropdown menu from the UI. 



# Criteria D: Functionality

## Video showcasing the functionality of the application

# Citation

1. O&#39;Neil, Lauren. “The Top 10 Ski and Snowboard Stores in Toronto.” blogTO, blogTO, 25 Nov. 2017, www.blogto.com/sports_play/2015/01/the_top_10_ski_and_snowboard_stores_in_toronto/.
2. “Python vs Swift: Which Language Is Better to Learn.” Cleveroad Inc. - Web and App Development Company, www.cleveroad.com/blog/python-vs-swift/. Accessed 25 Feb. 2024.
3. “What Is Kivy?: Need and Importance: Advantages and Disadvantages.” EDUCBA, 3 Apr. 2023, www.educba.com/what-is-kivy/.
4. LLP, Inexture Solutions. “Why Should You Choose Python for Mobile App Development?” YourStory.Com, 21 May 2020, yourstory.com/mystory/choose-python-mobile-app-development.
5. Qasim. “Understanding Sqlite vs Mysql: Comparing Databases for 2024.” RedSwitches, 31 Jan. 2024, www.redswitches.com/blog/sqlite-vs-mysql/. 
