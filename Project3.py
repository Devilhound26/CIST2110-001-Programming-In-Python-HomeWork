#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author:Jonathan Welch
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements: 
def import_Project3Tests():
    pass

import pytest 

print 
    
# OUTLINE - The LMS will consist of the following classes and methods:


# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. isbn (int)
#    b. title (string)
#    c. author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. check_out - sets borrowed to True and returns a message that the book has been checked out
#    c. check_in - sets borrowed to False and returns a message that the book has been checked in
#    d. borrowed - returns True if the book is borrowed and False if the book is not borrowed
# Replace the undefined variable "isbn" with a valid value or remove the line if it is not needed.
class Book:
    def __init__(self, isbn, title, author, borrowed):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.borrowed = borrowed

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"

    def check_out(self):
        self.borrowed = True
        return f"The book {self.title} has been checked out."

    def check_in(self):
        self.borrowed = False
        return f"The book {self.title} has been checked in."

    def is_borrowed(self):
        return self.borrowed


# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. name (string)
#    c. member_id (int)
#    d. borrowed_books (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
def _INIT_(self, name, member_id, borrowed_books):
    self.name = name
    self.member_id = member_id
    self.borrowed_books = borrowed_books


# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
#    c. return_book - removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)


# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Library:
    def __init__(self, books, users):
        self.books = books
        self.users = users

    def __str__(self):
        return f"Books: {self.books}, Users: {self.users}"

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

    def find_user(self, member_id):
        for user in self.users:
            if user.member_id == member_id:
                return user

    def export_books_to_csv(self, filename):
        with open(filename, "w") as file:
            file.write("ISBN,Title,Author,Borrowed\n")
            for book in self.books:
                file.write(f"{book.isbn},{book.title},{book.author},{book.borrowed}\n")

    def export_users_to_csv(self, filename):
        with open(filename, "w") as file:
            file.write("Name,ID,Borrowed Books\n")
            for user in self.users:
                borrowed_books_titles = [book.title for book in user.borrowed_books]
                file.write(
                    f"{user.name},{user.member_id},{','.join(borrowed_books_titles)}\n"
                )


# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
#    b. add_book - adds a book to the books list (should take a book as a parameter)
#    c. add_user - adds a user to the users list (should take a user as a parameter)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles

# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit
add_book = []
add_user = []
delete_book = []
delete_user = []
borrow_book = []
return_book = []
search_book = []
check_book = []
search_user = []
export_book = []
export_user = []
exit = []
print("Welcome to the Library Management System (LMS)")
print("Please select an option from the menu below:")
print("a. Add books")
print("b. Add users")
print("c. Delete books")
print("d. Delete users")
print("g. Borrow books")
print("h. Return books")
print("i. Search books")
print("j. Check if book is available")
print("k. Search users")
print("l. Export books to csv")
print("m. Export users to csv")
print("z. Exit")
menu = input("Please select an option from the menu above: ")
if menu == "a":
    add_book.append("a")
    print("You have selected to add a book.")
    print("Please enter the following information:")
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    borrowed = input("Borrowed: ")
    print("Book added successfully!")
elif menu == "b":
    add_user.append("b")
    print("You have selected to add a user.")
    print("Please enter the following information:")
    name = input("Name: ")
    member_id = input("ID: ")
    borrowed_books = input("Borrowed Books: ")
    print("User added successfully!")
elif menu == "c":
    delete_book.append("c")
    print("You have selected to delete a book.")
    print("Please enter the following information:")
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    borrowed = input("Borrowed: ")
    print("Book deleted successfully!")
elif menu == "d":
    delete_user.append("d")
    print("You have selected to delete a user.")
    print("Please enter the following information:")
    name = input("Name: ")
    member_id = input("ID: ")
    borrowed_books = input("Borrowed Books: ")
    print("User deleted successfully!")
elif menu == "g":
    borrow_book.append("g")
    print("You have selected to borrow a book.")
    print("Please enter the following information:")
    name = input("Name: ")
    member_id = input("ID: ")
    borrowed_books = input("Borrowed Books: ")
    print("Book borrowed successfully!")
elif menu == "h":
    return_book.append("h")
    print("You have selected to return a book.")
    print("Please enter the following information:")
    name = input("Name: ")
    member_id = input("ID: ")
    borrowed_books = input("Borrowed Books: ")
    print("Book returned successfully!")
elif menu == "i":
    search_book.append("i")
    print("You have selected to search for a book.")
    print("Please enter the following information:")
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    borrowed = input("Borrowed: ")
    print("Book found successfully!")
elif menu == "j":
    check_book.append("j")
    print("You have selected to check if a book is available.")
    print("Please enter the following information:")
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    borrowed = input("Borrowed: ")
    print("Book checked successfully!")
elif menu == "k":
    search_user.append("k")
    print("You have selected to search for a user.")
    print("Please enter the following information:")
    name = input("Name: ")
    member_id = input("ID: ")
    borrowed_books = input("Borrowed Books: ")
    print("User found successfully!")
elif menu == "l":
    export_book.append("l")
    print("You have selected to export books to csv.")
    print("Please enter the following information:")
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    borrowed = input("Borrowed: ")
    print("Books exported successfully!")
elif menu == "m":
    export_user.append("m")
    print("You have selected to export users to csv.")
    print("Please enter the following information:")
    name = input("Name: ")
    member_id = input("ID: ")
    borrowed_books = input("Borrowed Books: ")
    print("Users exported successfully!")
elif menu == "z":
    exit.append("z")
    print("You have selected to exit.")
    print("Goodbye!")
else:
    print("Invalid selection. Please try again.")
    
# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 11)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?


def main():
    pass  # Remove this line when you implement this method


if __name__ == "__main__":
    main()
