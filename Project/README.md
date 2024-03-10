# Unit 3: Online Order Tracker System for a Snowboard Company

![image](https://github.com/yuxuantaoisak/unit_3/assets/144768397/462102b4-c63c-49c3-96c4-1a441f8cebff)
*blogto.com* [1]


# Criteria A: Planning


## Problem Definition


My client is a snowboard factory owner. He is passionate about making various kinds of snowboards for snowboarders of all levels. However, he has recently encountered some problems with the management of his factory. Because of the increase in the number of clients, he is having some difficulties managing the online orders. He tried to write down order details for his employees to send packages everyday, but it does not work anymore with the huge increase in order numbers. Moreover, this triggers a problem: the employees now know all the trade secrets of the company, such as the revenue of the company. If the problem keeps getting worse, my client faces consequences such as losing customers, losing revenue, losing reputation in the industry, and the customer loyalty that he just built recently.


## Proposed Solution


Considering the problems that my client is facing, I will develop a manual program with a GUI(Graphical User Interface) for the client and his employees to track online orders, while providing the manager and employees with different user accesses. The order details with various attributes will be stored in an online database. This program will be developed using KivyMD, Python, and SQLite. 

The application will have a GUI output instead of a text output in order to meet the client's requirement of organizing the details of online orders into tables. Additionally, with a GUI that represents data in a visually attractive way, my client can understand and manage orders easily. 

Since my client has a MacBook Pro, the application can be developed using either Xcode or Python. I decided to use Python because of its popularity, community support, and a variety of Python libraries[2]. The large number of developers using Python makes it an easy-to-understand language. The upcoming programmers will easily understand the code so that they can make further improvements. Thus, Python is an appropriate choice for developing the application. 

Regarding the application interface, I decided to use KivyMD. KivyMD is a Python-based framework for the development of user interfaces. It has various bult-in widgets that can be easily changed and customized[3]. This allows my client to have a better user experience with the application. Additionally, KivyMD offers much better consistency than other cross-platform GUI toolkit like PyQT[4]. KivyMD is very unlikely to get crashed or hacked, which allows my client to build customer trust and reputation in the snowboard industry. Thus, KivyMD is adequate for the development of this application. 

Lastly, I chose SQLite as the database for the application. SQLite is a relational database. It's free to use so it does not cost any extra for my client. Moreover, SQLite is a good fit for embedded applications: it requires minimum setup and configuration settings so my client does not need to waste time on setting up his devices. So, SQLite is a better choice for the relational database management system in developing this application.



## Success Criteria


1. The GUI application has a secure login and registration system. [issue tackled: "I want the company's privacy and the order details to be secured. "]
2. The GUI application has different accesses for the admin and other users. [issue tackled: "Functions that have something to do with the company's privacy should be exlusive to me. "]
3. The GUI application provides a window to create and delete orders where the user can enter attributes including customer's name, items purchased, address, and time. [issue tackled: "I want a system to help me manage online orders. "]
4. The application provides a tracker where the user can check or add the quantity of all products. [issue tackled: "I also need to check and change the quantity of current products. "]
5. The GUI application provides a window to check revenue represented by a diagram that is exclusive to the admin. [issue tackled: "For example, I need to check the profit generated that is only accessible for me. "]
6. The GUI application provides customization function for the user to change the design of the snowboard according to their likings. [issue tackled: "The current model doesn't fit me. "]



# Criteria B: Solution Overview

## System diagram

![Screenshot 2024-03-07 at 23 40 14](https://github.com/yuxuantaoisak/unit_3/assets/144768397/7f39006b-09a3-4ee9-a61f-a26daf536ce6)

The above diagram illustrates the system, its parts, inputs, and output. The relationships between them are shown as well. The application takes user input from the keyboard and mouse, the computer details and the software it's running are included in the diagram. The python environment is PyCharm, in which two coding languages, python and KivyMD are ran. They interact with the relational database "project_3.db" inside the PyCharm environment. The output is displayed on a screen. 

## Wireframe diagram

![Screenshot 2024-03-10 at 0 43 27](https://github.com/yuxuantaoisak/unit_3/assets/144768397/da86f3b9-3220-4d35-8793-6e16e34b3ca7)

This is the wireframe diagram that shows the switch between screens in my application. The arrows and lines show which screen the application will switch to after pressing the button. 


## ER diagram

![Screenshot 2024-03-10 at 1 20 29](https://github.com/yuxuantaoisak/unit_3/assets/144768397/a96a79da-247e-4db4-bb44-f157278487de)

This ER diagram shows the tables in the database "project_3.db" and there relationships. As indicated, the table "orders" has 7 columns: id, customer_name, item_purchased, time_purchased, signature, address, amount. The other two tables have columns with specific data types like "text" and "int". The diagram also shows the relationship between items and orders: one order has one item. 


## UML diagram


![Screenshot 2024-03-10 at 2 00 13](https://github.com/yuxuantaoisak/unit_3/assets/144768397/ee68352c-808f-411d-a222-98fc819fbb9e)

This UML diagram shows the classes and their methods used in developing this application. The lines and arrows illustrate the inheritance relationship. Most of the classes used in the application either inherit from MDScreen class or MDApp class. 


![Blank diagram - Color (2)](https://github.com/yuxuantaoisak/unit_3/assets/144768397/3cfe411e-4db7-42d0-8d8f-37df5f605535)


## Flow diagrams


### delete order


![Blank diagram - Color (4)](https://github.com/yuxuantaoisak/unit_3/assets/144768397/d8c2288e-f6f7-48ab-9a17-91138a5f6ec8)

This is the flow diagram for the delete method inside the CheckOrder class. The method first checks if the user has selected a row (order). If so, it uses a for loop in which the database is connected and the orders are deleted according to their IDs. After performing the for loop, a MDDialog shows up, telling the user that the order has been deleted. 



### get_items

![Blank diagram - Color (5)](https://github.com/yuxuantaoisak/unit_3/assets/144768397/97624cde-ed2b-44e0-99b9-1a99c1ecf4f3)

The get_items method is used to get all the items from the database in order to generate the dropdown menu used when the user selects which item to add to the order in AddOrder class. The method first connects to the database, defines items as the result of the search, and menu_items as an empty list. Then it uses a for loop to get all the names of the item from the item variable. Another for loop is used to generate a dicitonary for the dropdown menu with all the names appended. Finally, a dropdown menu will pop up, allowing the user to select an item. 



### try_signup


![Blank diagram - Color (3)](https://github.com/yuxuantaoisak/unit_3/assets/144768397/38b62483-0197-48fb-888e-21bfe7245ead)

This method is called when the user tries to signup. It first defines upass, cpass, and email. Then, it uses a series of elif statements to confirm if the password policy is met. If so, two queries will be ran to check in the database if the email or username has been used. If not, the user information will be inserted into the database, followed by a pop up window saying that registration is complete. 




## Test plan



| N.o | Test type           | Description               | Process                                                                                                                                                                                                                         | Expected output                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----|---------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Unit testing        | Test for signup system    | 1, run the python file "project_3.py" 2, click "new user" button on the left 3, enter appropriate information to the textfields 4, click signup button                                                                          | If the username or the email is already used, the helper text will remind the user that they are used. If there is no "@" sign in email, the helper text will remind the user as well. If the password confirmation doesn't match, the helper text will remind the user. Otherwise, a pop up window will show up, saying that the registration is complete.                                                                                 |
| 2   | Unit testing        | Test for admin signup     | 1, run the python file "project_3.py" 2, click "new user" button on the left 3, click "admin signup" button in the  middle 4, enter appropriate information to the textfields 5, click signup button                            | If the username or the email is already used, the helper text will remind the user that they are used. If there is no "@" sign in email, the helper text will remind the user as well. If the password confirmation doesn't match, the helper text will remind the user. If the admin password is not correct, the helper text will say "access denied". Otherwise, a pop up window will show up, saying that the registration is complete. |
| 3   | Unit testing        | Test for login system     | 1, run the python file "project_3.py" 2, enter the account information 3, click login button                                                                                                                                    | If the user doesn't exist, or the password is incorrect, the helper text will remind the user. Otherwise, a pop up window will show up, and screen will be changed to home page.                                                                                                                                                                                                                                                            |
| 4   | Integration testing | Test for adding order     | 1, run the python file "project_3.py" 2, enter the account information 3, click login button 5, click the add order icon  6, enter appropriate information for the order 7, click save                                          | If the selection is empty, a pop up window  will remind the user to select an item to  include in the order. Otherwise, the order will be saved, and a pop up window will say that order is successfully saved.                                                                                                                                                                                                                             |
| 5   | Integration testing | Test for deleting order   | 1, run the python file "project_3.py" 2, enter the account information 3, click login button 4, click the order icon on home page 5, click the check order icon 6, select a row from the table 7, click the trash can to delete | If the selection is empty, a pop up window will remind the user to select a row.  Otherwise, the row will be deleted with a pop up window saying that the row is successfully deleted.                                                                                                                                                                                                                                                      |
| 6   | Integration testing | Test for check items page | 1, run the python file "project_3.py" 2, enter the account information 3, click login button 4, click the list icon on home page 5, click add mark on the right                                                                 | The quantity should be added one everytime the add button is pressed.                                                                                                                                                                                                                                                                                                                                                                       |
| 7   | Integration testing | Test for customize page   | 1, run the python file "project_3.py" 2, enter the account information 3, click login button 4, click the tool icon on home page 5, choose color and model, and click save                                                      | If the selection is empty, a pop up window will remind the user to select a color/model.  Otherwise, a popup window will say that the design is saved.                                                                                                                                                                                                                                                                                      |
| 8   | Integration testing | Test for profit graph     | 1, run the python file "project_3.py" 2, enter the account information of an admin account 3, click login button4 4, click the cash icon on home page                                                                           | A graph with a curve that represents revenue should show up.                                                                                                                                                                                                                                                                                                                                                                                |
| 9   | Unit testing        | Test for logout           | 1, run the python file "project_3.py" 2, enter the account information 3, click login button 4, click logout icon on home page                                                                                                  | A pop up window will show up, asking for the confirmation of logging out.                                                                                                                                                                                                                                                                                                                                                                   |
| 10  | Code review         | Review all codes          | 1, open "project_3.py" 2, open "project_3.kv" 3, check all lines 4, make changes if needed                                                                                                                                      | All codes should be commented thoroughly, with a structure that can be easily understood and followed.                                                                                                                                                                                                                                                                                                                                      |


## Record of tasks



| Task No | Planned action                         | Planned outcome                                                                              | Time estimate | Completion date | Criterion |
|---------|----------------------------------------|----------------------------------------------------------------------------------------------|---------------|-----------------|-----------|
| 1       | First meeting with the client          | Talk to the client and identify the problems he is facing.                                   | 15 mins       | Jan 25, 2024    | A         |
| 2       | Write problem definition               | The client's problem clearly defined                                                         | 20 mins       | Feb 1, 2024     | A         |
| 3       | Brainstorm and come up with a solution | The outline of proposed solution                                                             | 20 mins       | Feb 7, 2024     | A         |
| 4       | Write proposed solution                | A detailed proposed solution, including clear justification of the tools used                | 40 mins       | Feb 10, 2024    | A         |
| 5       | Second meeting with the client         | Show the client the proposed solution  and finalize success criteria                         | 15 mins       | Feb 11, 2024    | A         |
| 6       | Success criteria                       | Come up with success criteria that the client approves                                       | 20 mins       | Feb 17, 2024    | A         |
| 7       | Diagram drawing                        | Draw system diagram                                                                          | 20 mins       | Feb 23, 2024    | B         |
| 8       | Diagram drawing                        | Wireframe diagram                                                                            | 20 mins       | Feb 24, 2024    | B         |
| 9       | Login and registration system UI       | Create the UI of login and registration page                                                 | 40 mins       | Feb 25, 2024    | C         |
| 10      | Login system code                      | Create a system that allows returning users to login                                         | 40 mins       | Feb 26, 2024    | C         |
| 11      | Registration system code               | Create a system that allows new users to register, including password policy                 | 1 hr          | Feb 27, 2024    | C         |
| 12      | Admin login code                       | Create a system to authenticate if the login user is admin or not                            | 20 mins       | Feb 28, 2024    | C         |
| 13      | Admin login UI                         | Create the UI of admin login page                                                            | 15 mins       | Feb 29, 2024    | C         |
| 14      | Admin signup code                      | Create a system that allows new users to sign up as an admin if authenticated                | 20 mins       | Feb 29, 2024    | C         |
| 15      | Admin signup UI                        | Create the UI of admin signup page                                                           | 10 mins       | Mar 1, 2024     | C         |
| 16      | Home page UI                           | Create the UI for home screen, including all the buttons                                     | 20 mins       | Mar 1, 2024     | C         |
| 17      | Order page UI                          | Create the UI for the order page, excluding the functions inside it                          | 20 mins       | Mar 1, 2024     | C         |
| 18      | Add order code                         | Create the code for add order function                                                       | 45 mins       | Mar 2, 2024     | C         |
| 19      | Create dropdown menu                   | Create the dropdown menu for add order function                                              | 20 mins       | Mar 2, 2024     | C         |
| 20      | Check order code                       | Create the page where the user can check or delete orders                                    | 30 mins       | Mar 2, 2024     | C         |
| 21      | Check order table                      | Create the table inside the check order page, which displays all the attributes of the order | 30 mins       | Mar 3, 2024     | C         |
| 22      | Check items code                       | Create the code for checking all items, including adding items quantity                      | 1 hr          | Mar 3, 2024     | C         |
| 23      | Customize page UI                      | Create the UI for customize page                                                             | 30 mins       | Mar 3, 2024     | C         |
| 24      | Customize page code                    | Create the code for customize page                                                           | 45 mins       | Mar 5, 2024     | C         |
| 25      | Customize page UI                      | Create the UI for customize page                                                             | 20 mins       | Mar 5, 2024     | C         |
| 26      | Check profit graph                     | Create the profit diagram function for admin users                                           | 20 mins       | Mar 6, 2024     | C         |
| 27      | Refine the application                 | Make adjustments to the layout, buttons, etc.                                                | 20 mins       | Mar 6, 2024     | C         |
| 28      | Minimum viable product                 | Make an MVP presentation to the client                                                       | 10 mins       | Mar 7, 2024     | A         |
| 29      | Diagram drawing                        | Draw ER diagram                                                                              | 20 mins       | Mar 7, 2024     | B         |
| 30      | Diagram drawing                        | Draw UML diagram                                                                             | 20 mins       | Mar 7, 2024     | B         |
| 31      | Diagram drawing                        | Draw Flow diagrams                                                                           | 20 mins       | Mar 7, 2024     | B         |
| 32      | Test plan                              | Create a test plan                                                                           | 45 mins       | Mar 9, 2024     | B         |
| 33      | Documentation                          | Finish criteria C documentations                                                             | 2 hr          | Mar 9, 2024     | C         |
| 34      | Record demonstration video             | Finish criteria D functionalities                                                            | 5 mins        | Mar 10, 2024    | D         |
| 35      | Final presentation                     | Make the final presentation to the client                                                    | 10 mins       | Mar 11, 2024    | A         |



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

After confirming that all requirements are met, the try block was used to insert the information, including username, email, password, and admin status into the database "project_3.db" using the DatabaseBridge class. The password is encrypted by the get_hash method I imported. The admin status is automatically set as 0, or false (the SQLite database does not accept Boolean value, so I had to use 0 and 1 to represent true and false), since this is the signup page for normal users. Then, a pop up window will show that the user has successfully signed up. The window will automatically jumps to login page after that.

### get_hash

As shown above, the password entered by the user during registration is stored into the database after being encrypted by a method called get_hash. 

```.py

hash_function = sha256_crypt.using(rounds=30000)


def get_hash(text: str):
    return hash_function.hash(text)


```

The get_hash function takes a string as the input, pads the input message, divides it into 512-bit blocks, and processes each block through 64 rounds of a compression function. This function applies bitwise operations and additions using an initial hash value to produce a 256-bit hash output, ensuring data integrity and security through a computationally irreversible process. In this case, the password is encrypted using this method before it is stored into the database so that even the database is hacked, the passwords will still stay safe. 



## Admin Signup

As part of my client's requirement, the admin user should be provided with extra functions. Thus, I designed a signup window that is exclusively for the admin user. The admin signup page asks for an extra admin password, which is set by the company owner and validates the current user's identity. This password that allows the user to sign up as an admin is set by the owner of the snowboard company. If the user enters the correct admin password, the system can confirm that they are authorized by the owner to sign up as an admin with the access to extra functions. 

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


### Validating password

Since the password is not directly stored into the database as it appears, the check_hash method must be used to validate the password. It compares a hash and a original text to see if they match, and return true or false. Here, it must return true for the program to proceed. 


### Confirming admin status

The code confirms the admin status of the user, which is either 0 or 1. 

As the code shows, if the admin status is 0 (false), the user will jump to home page for normal users, while the page turns to admin home page if admin status is 1 (true). With this design, the user can go to their respective home pages without entering extra information on their admin status, as the system automatically communicates with the SQL database to confirm the user's admin status. 

Also, the LoginPage.admin class variable is defined as True if the user logs in as an admin. This variable can be passed and used in other classes in order to confirm whether the current user is an admin or not, and further display corresponding pages and functions according to their status.  



![Screenshot 2024-03-07 at 0 26 59](https://github.com/yuxuantaoisak/unit_3/assets/144768397/fefa0b9e-a791-47fd-bcb5-18892632b3ba)



_Fig. 1_


**Fig. 1** is a snapshot of the user entity in the database. As shown in the photo, the passwords are encrypted so that they won't get leaked even if people outside the company see this page, making the users' information more secure. Also, the admin status is recorded as either 0 or 1.


### change_page method

This method uses the class variable from the LoginPage class. The admin status is confirmed when the user logs in and stored into the LoginPage.admin variable. 


```.py

def change_page(self):
    if LoginPage.admin is True:
        self.parent.current = "AdminHome"
    else:
        self.parent.current = "HomePage"

```

On the order page, the user is directed to either add order page or check order page. When the user wants to go back to the home page, this method will decide which home page (admin or normal) to take the user to according the variable LoginPage.admin that is defined when the user logs in. 



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


Note that the KivyMD part of this code is omitted. Check the MDDropDownMenu element in the kivy file section. 



### Choose date

In the add order page, I designed a button where the user can select the date when the order is received using the MDDatePicker dialog box from KivyMD library. 

```.py

def choose_date(self):
    date_dialog = MDDatePicker()
    date_dialog.bind(on_save=self.on_save)
    date_dialog.open()

def on_save(self, instance, value, date_range):
    self.selected_date = value
    value = value.strftime("%m/%d/%Y")
    self.ids.time_purchased.text = f"{value}"

```

The choose_date method is called when the user clicks the button. The method creates an instance of MDDatePicker which is a graphical calender that allows the user to pick a date from. The bind method is used to connect the event selected, which is the date in this case. Then, the on_save method first stores the selected date into the value variable, which then is formatted as "mm/dd/yyyy". The date on display in the GUI then becomes the date that the user selected. 


The choose date method helps user picking a date when the order is received, effectively documenting order details. The use of MDDatePicker enhances user experience by a better design, and an easy way to select date. 



## Check order page


On this page, I designed a table where the user can check all the orders. When they finish mailing an order, they can choose to delete it from the list. 

<img width="380" alt="Screenshot 2024-03-08 at 0 13 16" src="https://github.com/yuxuantaoisak/unit_3/assets/144768397/5de2ceab-e747-49e4-83aa-ec9b9f10efd1">

The picture demonstrates what the table looks like in the GUI. 

### Deleting order

```.py

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

```

When the user tries to delete order(s), the delete method in CheckOrder class is called. First, it confirms the rows that the user checked by ticking the boxes. If the user didn't select any rows, a pop up window will remind that a row has to be selected to delete. Otherwise, the DatabaseBridge class is used to interact with the relational database, after which a SQL query to delete the row is ran. Then, a pop up window will show up to let the user know that the order is deleted. 

The table is immediately refreshed using the update method from the same class. 


## Check items page

As required by the client, I designed a page in which the user can check and add the current quantity of all products. In the CheckItemsPage class, a query that searches for the "quantity" column in the "items" table is ran for each product. The result is saved into a variable and converted into a list by the built-in list() function to make it subscriptable. The original data type is "tuple", which is not subscriptable, preventing me from getting the quantity number. 

This is an example of how I achieve this. 

```.py

def on_pre_enter(self, *args):

    db = DatabaseBridge("project_3.db")

    query_neck_warmer = f"""SELECT quantity FROM items WHERE id = 1"""
    self.neck_warmer = list(db.search(query=query_neck_warmer, multiple=False))
    self.ids.neck_warmer.text = f"Quantity: {str(self.neck_warmer[0])}"

    #  code omitted for the purpose of displaying the strcture

```

As shown in the code, after getting the quantity of the product, the text on the GUI displays the result as it appears in the database, allowing the user to get a sense of the number of products currently in stock. Note that the code is repeated for each product. 



In order to display the correct quantity, the quantity needs to be subtracted one each time the user adds an order with that product. To achieve this, I modified the save method in the AddOrder class. 

```.py

def save(self):

    #  code omitted

    db = DatabaseBridge("project_3.db")
    query_item = f"""UPDATE items SET quantity = quantity - 1 WHERE item_name = '{items_purchased}'"""

    db.run_query(query=query_item)

```


With this change, the quantity adheres to the real quantity so that it changes whenever a user adds an order. 


## Plotting revenue graph

As part of this project's success criteria, there should be a function to check revenue graph that is exclusive to the admin user. I defined a method under the class `AdminHome` so that only admin user has the access to it. 

```.py

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

```

This method first connects to the database, and used a inner join clause from SQL queries. Inner join clause selects records that have matching values in both tables. Here, all the same values from item_name column in `items` table and item_purchased column in `orders` table are selected, along with profit and time. 

With these information, the profit and dates are appended to two empty lists in a for loop. Then, matplotlib library is used to plot the graph. 


## Kivy file: "project_3.kv"

### Screen manager

```.kv

ScreenManager:

    id: screens

    LoginPage:
        name: "LoginPage"

    SignupPage:
        name: "SignupPage"

    AdminSignup:
        name: "AdminSignup"

    HomePage:
        name: "HomePage"

    OrderPage:
        name: "OrderPage"

...

```

The screen manager funtion of KivyMD makes it easy to swtich between screens that inhert from MDScreen class. Eacy screen is named accordingly and assigned a unique id (name) so that they each have different functionalities and layout. This allows me to build the application across different screens with different functions, which makes it more user friendly. 


### FitImage

FitImage is a widget provided by KivyMD library for the purpose of displaying an image in the KivyMD application. The primary function of FitImage is to fit the displayed image within the available space while preserving its aspect ratio. This means that the image will be scaled to fit the available area without distortion. FitImage is particularly useful when you want to display images in a way that ensures they are fully visible without stretching or cropping. In my application, I used FitImage for my background image. 

```.kv

FitImage:
        source: "background.jpg"

```

### MDDialog

To make the application interactive and let the user aware of what's happening, I used a MDDialog which is a KivyMD box component. 

For example, this is a pop up window constructed with MDDialog. It appears after the user successfully logs in. 

```.kv

dialog = MDDialog(title="Logged in", text=f"{uname}, you successfully logged in!")
dialog.open()

```

MDDialog can take different inputs as well. On the home page, I designed a pop up window with two MDFlatButtons, which shows up when the user clicks logout. The texts on the button are yes and no, each calling another method to either confirm or cancel logout. This ensures that the user doesn't accidentally logout. 



### MDCheckBox


```.kv

MDBoxLayout:
    size_hint: .8, .07
    pos_hint: {"center_x": .5}

    MDCheckbox:
        id: showpassword
        size_hint: .1, 1
        pos_hint: {"center_x": .5,"center_y": .5}
        on_active: root.show_password()


```


The MDCheckBox widget is assigned with the id "showpassword", and specified its size and position by `size_hint` and `pos_hint` attributes. The `on_active` event of the MDCheckBox calls the `show_password` method from the main python file: whenever the checkbox is toggled (selected or unselected), the `show_password` method is called to show or hide the password. 



### MDIconButton

MDIconButton is a Kivymd component that allows me to build a button that is represented by an icon. With this, I can now design a minimalistic style button which greatly improves user experience and simplifies the UI page. 

```.kv

MDIconButton:
    icon: "shopping-outline"
    text: "Orders"
    md_bg_color: "#1f7fed"
    size_hint: .4, .05
    pos_hint: {"center_x": .5, "center_y": .5}
    on_release: app.root.current = 'OrderPage'

```

Above is an example of the use of MDIconButton in my application. I used the "shopping-outline" icon which looks like a shopping bag. The user can instinctively understand the meaming behind this icon. 


### MDDropDownMenu


```.py

buttons_menu = []

for name in self.menu_items:
    btn_dict = {"text": str(name),
                "viewclass": "OneLineListItem",
                "on_release": lambda x=name: self.button_pressed(x)}
    buttons_menu.append(btn_dict)

self.menu = MDDropdownMenu(caller=button, items=buttons_menu,
                                   width_mult=4)
self.menu.open()

```

I used the MDDropDownMenu component to build the dropdown list where the user can select the item in the order. All the names of the item are already stored into the variable `self.menu_items` in the previous part of the code. Here, I used a for loop to append the "text", "viewclass", and "on_release" attributes of the dropdown menu to an empty list called `buttons_menu`. The `on_release` attribute calls the button_pressed method in the same class which selects the row that the user clicked and print it. Then, the MDDropDownMenu element is used, which automatically generates a dropdown list given the information. 


### MDColorPicker

In the customize page, I designed a color picker so that the user can pick desired color from a visually beautified and user-friendly color picker. 

```.py

def open_color_picker(self):
    color_picker = MDColorPicker(size_hint=(0.45, 0.85))
    color_picker.open()
    color_picker.bind(
    on_select_color=self.on_select_color,
    on_release=self.get_selected_color,
    )

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


```


This code defines a method `open_color_picker` that initializes a color picker widget (`MDColorPicker`) and binds two events to it: `on_select_color` and `on_release`. When a color is selected within the picker, the `get_selected_color` method is called to print the selected color and update the background color of a toolbar element (`self.ids.toolbar`). The `update_color` method adjusts the alpha channel of the selected color and applies it to the toolbar. 


With this design, the user can now pick a color easily from a range of choices displayed on a palette for their personalized snowboard. 



# Criteria D: Functionality

## Video showcasing the functionality of the application

https://youtu.be/TEr3MkY2x_o


# Citation

1. O&#39;Neil, Lauren. “The Top 10 Ski and Snowboard Stores in Toronto.” blogTO, blogTO, 25 Nov. 2017, www.blogto.com/sports_play/2015/01/the_top_10_ski_and_snowboard_stores_in_toronto/.
2. “Python vs Swift: Which Language Is Better to Learn.” Cleveroad Inc. - Web and App Development Company, www.cleveroad.com/blog/python-vs-swift/. Accessed 25 Feb. 2024.
3. “What Is Kivy?: Need and Importance: Advantages and Disadvantages.” EDUCBA, 3 Apr. 2023, www.educba.com/what-is-kivy/.
4. LLP, Inexture Solutions. “Why Should You Choose Python for Mobile App Development?” YourStory.Com, 21 May 2020, yourstory.com/mystory/choose-python-mobile-app-development.
