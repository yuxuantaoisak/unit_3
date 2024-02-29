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



1. The GUI application has a login and registration system secured by the hash function. [issue tackled: "I want the customers' privacy and order details to be secured"]
2. The GUI application provides a window to create snowboards where the user can enter attributes including color, material, price, and number. [issue tackled: ""]
3. The GUI application provides a window to create orders where the user can enter attributes including customer's name, items purchased, address, and total amount. [issue tackled: ""]
4. The application provides a money tracker in which the user can check the profit represented by a diagram. [issue tackled: ""]
5. The GUI application provides different user accesses to private information like revenue and customer data for the company owner and other employees. [issue tackled: ""]
6. The GUI application provides customization function for the user to change the design of the snowboard according to their likings. [issue tackled: ""]



# Criteria B: Solution Overview

## System diagram

## Wireframe diagram

## ER diagram

## UML diagram

## Flow diagrams

## Test plan

## Record of tasks



# Criteria C: Development

## Existing tools

## List of techniques used

# Criteria D: Functionality

## Video showcasing the functionality of the application

# Citation

1. O&#39;Neil, Lauren. “The Top 10 Ski and Snowboard Stores in Toronto.” blogTO, blogTO, 25 Nov. 2017, www.blogto.com/sports_play/2015/01/the_top_10_ski_and_snowboard_stores_in_toronto/.
2. “Python vs Swift: Which Language Is Better to Learn.” Cleveroad Inc. - Web and App Development Company, www.cleveroad.com/blog/python-vs-swift/. Accessed 25 Feb. 2024.
3. “What Is Kivy?: Need and Importance: Advantages and Disadvantages.” EDUCBA, 3 Apr. 2023, www.educba.com/what-is-kivy/.
4. LLP, Inexture Solutions. “Why Should You Choose Python for Mobile App Development?” YourStory.Com, 21 May 2020, yourstory.com/mystory/choose-python-mobile-app-development.
5. Qasim. “Understanding Sqlite vs Mysql: Comparing Databases for 2024.” RedSwitches, 31 Jan. 2024, www.redswitches.com/blog/sqlite-vs-mysql/. 
