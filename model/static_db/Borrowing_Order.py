
class BorrowingOrder:
    def __init__(self, order_id, date, client_id, book_id, status):
        self.__id = order_id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status

    def get_order_info(self):
        return f"Order id: {self.__id}, date: {self.__date}," \
               f" status: {self.__status}, client id: {self.__client_id}, book id: {self.__book_id}"

    def get_client_id(self):
        return self.__client_id

    def get_id(self):
        return self.__id

    def get_status(self):
        return self.__status

    def get_info_for_orders(self):
        return f"Order id: {self.get_id()}, date: {self.__date}, status: {self.__status}, book id: {self.__book_id}"

    def set_status(self, status):
        self.__status = status

    def get_book_from_order(self):
        return self.__book_id


