

class Book:
    def __init__(self, book_id: int, title: str, description: str, author: str, status: str):
        self.__id = book_id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def get_books_info(self):
        return f"Book id: {self.__id}, Title: {self.__title}, Description: {self.__description}," \
               f" author: {self.__author}, status: {self.__status}"

    def get_id(self):
        return self.__id

    def get_status(self):
        return self.__status
#

    def check_id(self, book_id):
        if self.__id == book_id:
            return True

    def book_return_1(self, book_id):
        if self.__id == book_id:
            return True
#

    def set_book_status(self, status):
        self.__status = status

# do not forget controller
