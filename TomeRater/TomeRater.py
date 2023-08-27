class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("this user's email has been updated")

    def __repr__(self):
        return "User : {0}, email : {1}, books read : {2}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name & self.email == other_user.email
    
    def read_book(self, book, rating = None):
        self.books[book] = rating
    
    def get_average_rating(self):
        if len(self.books) > 0:
            _sum = 0
            for rating in self.books.values():
                if rating is not None:
                    _sum += rating
            return _sum/len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN for the book with title: {0} has been updated.".format(self.title))

    def add_rating(self, rating):
        if rating is not None:
            if 0 <= rating <= 4 :
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title & self.isbn == other_book.isbn

    def get_average_rating(self):
        if len(self.ratings) > 0:
            _sum = 0
            for x in self.ratings:
                _sum += x
            return _sum/len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{0} with ISBN: {1}".format(self.title, self.isbn)

class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{0} by {1}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

    def __repr__(self):
        return "{0}, a {1} manual on {2}".format(self.title, self.level, self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {} # an empty dictionary that will map a user’s email to the corresponding User object
        self.books = {} # an empty dictionary that will map a Book object to the number of Users that have read it
        self.added_books = [] # an empty list is to keep all added book to the TomeRater object

    def create_book(self, title, isbn):
        if self.Is_Unique_ISBN(isbn) is True:
            book = Book(title, isbn)
            self.added_books.append(book)
            return book
        else:
            print("ISBN : {0} is not unique, book {1} is not created.".format(isbn, title))
            return None

    def Is_Unique_ISBN(self, isbn):
        if len(self.added_books) > 0:
            for book in self.added_books:
                if book.isbn == isbn:
                    return False
        return True

    def create_novel(self, title, author, isbn):
        if self.Is_Unique_ISBN(isbn) is True:
            fiction = Fiction(title, isbn, author)
            self.added_books.append(fiction)
            return fiction
        else:
            print("ISBN : {0} is not unique, Novel {1} is not created.".format(isbn, title))
            return None

    def create_non_fiction(self, title, subject, level, isbn):
        if self.Is_Unique_ISBN(isbn) is True:
            non_fiction = Non_Fiction(title, isbn, subject, level)
            self.added_books.append(non_fiction)
            return non_fiction
        else:
            print("ISBN : {0} is not unique, Non Fiction {1} is not created.".format(isbn, title))
            return None

    def add_user(self, name, email, user_books = None):
        if email in self.users:
            print("{0} already exists".format(email))
        else:
            if self.Is_Valid_Email(email) is True:
                user = User(name, email)
                self.users[email] = user
                if user_books is not None:
                    for book in user_books:
                        if book is not None:
                            self.add_book_to_user(book, email)

    def Is_Valid_Email(self, email):
        if email.count('@') == 1:
            domains = ['.com', '.edu', '.org']
            for domain in domains:
                if domain in email and email[-4:] == domain:
                    return True
        print("{0} is invalid".format(email))
        return False

    def add_book_to_user(self, book, email, rating = None):
        if self.Is_Valid_Email(email) is True:
            user = self.users[email]
            if email in self.users:
                if book is not None:
                    user.read_book(book, rating)
                    book.add_rating(rating)
                    if book in self.books:
                        self.books[book] +=1
                    else:
                        self.books[book] = 1
            else:
                print("No user with email {0}!".format(email))

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_positive_user(self):
        _highest_avg_rating = 0
        _user = None
        for user in self.users.values():
            _avg_rating = user.get_average_rating()
            if _avg_rating is not None:
                if _avg_rating > _highest_avg_rating:
                    _highest_avg_rating = _avg_rating
                    _user = user
        return _user

    def highest_rated_book(self):
        _highest_avg_rating = 0
        _book = None
        for book in self.books.keys():
            _avg_rating = book.get_average_rating()
            if _avg_rating is not None:
                if _avg_rating > _highest_avg_rating:
                    _highest_avg_rating = _avg_rating
                    _book = book
        return _book

    def get_most_read_book(self):
        _highest_read = 0
        _book = None
        for book, rating in self.books.items():
            if rating > _highest_read:
                _highest_read = rating
                _book = book
        return _book

