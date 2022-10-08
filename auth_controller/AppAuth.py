from model.static_db.Book import Book
from model.static_db.Borrowing_Order import BorrowingOrder
from model.user_db.Client import Client
from model.user_db.Librarian import Librarian
from utils.Utils import Constants


class AppAuth:

    # clients id start with 1

    clients_list: list[Client] = [
        Client(client_id=101, id_no=1321565, name="Ahmed", age=22, client_phone=2284840),
        Client(client_id=102, id_no=1544818, name="Khaled", age=40, client_phone=262895),
        Client(client_id=103, id_no=1848945, name="Sameer", age=24, client_phone=6546568),
        Client(client_id=104, id_no=6456456, name="Sameer", age=24, client_phone=6549818),
        Client(client_id=105, id_no=6453775, name="Sameer", age=24, client_phone=5342532),
        Client(client_id=106, id_no=5324532, name="Sameer", age=24, client_phone=6547468),
        Client(client_id=107, id_no=1984769, name="Saeed", age=35, client_phone=2629815)
    ]

    # librarian id starts with 5

    librarian_list: list[Librarian] = [
        Librarian(libr_id=501, id_no=5498489, employment_type=Constants.FULL_TYPE, name="Khamees", age=39),
        Librarian(libr_id=502, id_no=1891915, employment_type=Constants.PART_TYPE, name="Hamada", age=35),
        Librarian(libr_id=503, id_no=8919189, employment_type=Constants.PART_TYPE, name="Mahmoud", age=32)
    ]

    # book id starts with 2

    book_list: list[Book] = [
        Book(book_id=201, title="Cosmos", description="Popular science", author="Carl Sagan", status=Constants.ACTIVE),
        Book(202, "Atomic habits", "Self-help", "James Clear", Constants.ACTIVE),
        Book(203, "Rich Dad Poor Dad", "Personal finance", "Robert Kiyosaki, Sharon Lechter", Constants.ACTIVE),
        Book(204, "why we sleep", "Science book", "Matthew Walker", Constants.ACTIVE),
        Book(205, "the power of habit", "Self-help", "Charles Duhigg", Constants.INACTIVE),
        Book(206, "So Good They Can’t Ignore You", "Self-help", "Cal Newport", Constants.INACTIVE),
        Book(207, "the 4 hour work week", "Self-help", "Tim Ferriss", Constants.INACTIVE),
        Book(208, "Book 8", "Art", "author 8", Constants.INACTIVE),
        Book(209, "Book 9", "Self-help", "author 9", Constants.ACTIVE),
        Book(210, "Book 10", "Science book", "author 10", Constants.ACTIVE),
        Book(211, "Book 11", "Self-help", "author 11", Constants.ACTIVE)
    ]

    # order id starts with 7

    orders_list: list[BorrowingOrder] = [
        BorrowingOrder(order_id=701, date="4/10/2022", client_id=102, book_id=205, status=Constants.ACTIVE),
        BorrowingOrder(order_id=702, date="7/9/2022", client_id=103, book_id=206, status=Constants.ACTIVE),
        BorrowingOrder(order_id=703, date="5/3/2022", client_id=106, book_id=207, status=Constants.ACTIVE),
        BorrowingOrder(order_id=704, date="1/2/2022", client_id=101, book_id=201, status=Constants.EXPIRED),
        BorrowingOrder(order_id=705, date="3/2/2022", client_id=101, book_id=202, status=Constants.CANCELLED),
        BorrowingOrder(order_id=706, date="8/2/2022", client_id=101, book_id=203, status=Constants.EXPIRED),
        BorrowingOrder(order_id=707, date="9/2/2022", client_id=107, book_id=208, status=Constants.ACTIVE)
    ]

    borrowed_orders: list[BorrowingOrder] = []

    borrowed_books: list[book_list] = []

    for item in orders_list:
        if item.get_status() == Constants.ACTIVE:
            borrowed_orders.append(item)

    total_borrowed_orders = len(borrowed_orders)

    for item in book_list:
        if item.get_status() == Constants.INACTIVE:
            borrowed_books.append(item)

    total_borrowed_books = len(borrowed_books)
    total_available_books = len(book_list) - total_borrowed_books

    def get_last_book_id(self) -> int:
        return self.book_list[len(self.book_list) - 1].get_id()

    def get_last_order_id(self) -> int:
        return self.orders_list[len(self.orders_list) - 1].get_id()

    def get_last_client_id(self) -> int:
        return self.clients_list[len(self.clients_list) - 1].get_id()

    def is_id_no_exist(self, id_no, client_list: list[Client]) -> bool:
        is_exist = False
        for item in client_list:
            if item.get_id_no() == id_no:
                is_exist = True
        return is_exist

    def is_book_active(self, book_id, book_list: list[Book]) -> bool:
        for item in book_list:
            if item.get_id() == book_id:
                if item.get_status() == Constants.ACTIVE:
                    item.set_book_status(Constants.INACTIVE)
                    return True
        return False

    def return_books(self, order_id, order_list: list[BorrowingOrder],
                     client_id, client_list: list[Client], book_list: list[Book]):
        for item in order_list:
            for item2 in client_list:
                if item.get_id() == order_id and item2.get_id() == client_id and item.get_status() == Constants.ACTIVE:
                    for item33 in book_list:
                        if item33.get_id() == item.get_book_from_order():
                            item.set_status(Constants.CANCELLED)
                            item33.set_book_status(Constants.ACTIVE)

    def gap_line(self):
        print("**************************************\n"
              "--------------------------------------\n"
              "**************************************")

