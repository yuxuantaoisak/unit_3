class Books:
    def __init__(self, title: str, author: str, price: int, rating: int, publisher: str):
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating
        self.publisher = publisher

    def get_title(self):
        return self.title

    def rate_a_book(self, new_rating: int):
        if 0 <= new_rating <= 10:
            self.rating = new_rating
        return self.rating

    def get_publisher(self):
        return self.publisher


secret_life_of_bees = Books(title="The secret life of bees", author="Sue Monk Kidd", price=50, rating=6, publisher="ISAK")
hunger_games = Books(title="The Hunger games", author="Collins", price=70, rating=9, publisher="Japan print")
harry_potter = Books(title="Harry potter", author="JKR", price=200, rating=10, publisher="UK print")

print(harry_potter.get_title())

