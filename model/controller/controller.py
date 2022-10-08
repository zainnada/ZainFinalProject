# doesn't work :(
# but it's ok, I understand its idea, and I will work with it in my future projects.

from main import my_auth, my_utils
from model.static_db.Book import Book
from utils.Utils import Constants


class LibraryController:

    # librarian input 1
    def view_all_books(self):
        for item1 in my_auth.book_list:
            print(item1.get_books_info())
            my_auth.gap_line()

    # librarian input 2

    def view_all_clients(self):
        for item1 in my_auth.clients_list:
            print(item1.get_clients_info())
        my_auth.gap_line()

    def add_book(self):

        book_id = my_auth.get_last_book_id() + 1
        title = input("Book title: ")
        description = input("Description: ")
        author = input("Author: ")
        status = Constants.ACTIVE

        if not my_utils.empty_checker(title, description, author):

            my_auth.book_list.append(Book(book_id=book_id, title=title,
                                          description=description, author=author, status=status))
            print("Done.")
            my_auth.gap_line()

        else:
            print("Error, empty value!")
            my_auth.gap_line()



