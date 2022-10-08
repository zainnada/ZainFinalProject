# Final Project: Library Program

from auth_controller.AppAuth import AppAuth
from model.static_db.Book import Book
from model.static_db.Borrowing_Order import BorrowingOrder
from model.user_db.Client import Client
from utils.Utils import Constants, Utils

my_auth = AppAuth()
my_utils = Utils()

print("********************************\n"
      "*      WELCOME TO LIBRARY      *\n"
      "********************************")

first_con = True
my_condition = False
while first_con:
    is_id_exist = False
    id_input = input("Enter your id: ")
    user_condition = True

    if not my_utils.empty_checker(id_input) and my_utils.digit_checker(id_input):
        id_input = int(id_input)
        my_condition = True
        for item in my_auth.librarian_list:

            if item.get_id() == id_input:
                my_condition = False
                while user_condition:
                    librarian_input = input("** Choose:"
                                            "\n1- Print the books"
                                            "\n2- Print the clients"
                                            "\n3- Add a new book"
                                            "\n4- Print the orders"
                                            "\n5- Print the clients and their orders"
                                            "\n6- Add a client"
                                            "\n7- Print the active orders"
                                            "\n8- Back to main"
                                            "\n9- Exit\n")

                    if not my_utils.empty_checker(librarian_input) and my_utils.digit_checker(librarian_input):
                        librarian_input = int(librarian_input)

                        if librarian_input == 1:
                            for item1 in my_auth.book_list:
                                print(item1.get_books_info())
                            my_auth.gap_line()

                        if librarian_input == 2:
                            for item1 in my_auth.clients_list:
                                print(item1.get_clients_info())
                            my_auth.gap_line()

                        elif librarian_input == 3:
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

                        elif librarian_input == 4:
                            for item1 in my_auth.orders_list:
                                print(item1.get_order_info())
                            my_auth.gap_line()

                        elif librarian_input == 5:
                            for item1 in my_auth.clients_list:
                                for item2 in my_auth.orders_list:
                                    if item1.get_id() == item2.get_client_id():
                                        print(item1.get_clients_info(), item2.get_order_info())
                            my_auth.gap_line()

                        elif librarian_input == 6:
                            new_con = True
                            client_id = my_auth.get_last_client_id() + 1
                            id_no = input("Client national id: ")
                            name = input("Client name: ")
                            age = input("Client age: ")
                            client_phone = input("Client phone: ")
                            if not my_utils.empty_checker(id_no, name, age, client_phone) and\
                                    my_utils.digit_checker(id_no):
                                id_no = int(id_no)
                                if not my_auth.is_id_no_exist(id_no=id_no, client_list=my_auth.clients_list):

                                    my_auth.clients_list.append(Client(client_id=client_id,
                                                                       client_phone=client_phone,
                                                                       name=name, age=age, id_no=id_no))
                                    print("Client is registered successfully.")
                                    my_auth.gap_line()
                                else:
                                    print("Client is not registered.")
                                    my_auth.gap_line()
                            else:
                                print("Error")
                                my_auth.gap_line()

                        elif librarian_input == 7:
                            for item22 in my_auth.borrowed_orders:
                                print(item22.get_order_info())

                        elif librarian_input == 8:
                            print("See you :)")
                            my_auth.gap_line()
                            user_condition = False

                        elif librarian_input == 9:
                            print("Don't leave me alone :(")
                            user_condition = False
                            first_con = False
                            # exit()

                        else:
                            print("Wrong choice")

                    else:
                        print("wrong entry")
                        my_auth.gap_line()

    if my_condition:
        for item in my_auth.clients_list:
            if item.get_id() == id_input:
                is_id_exist = True

                while user_condition:

                    client_input = input("** Choose:\n"
                                         "1- Print the books\n"
                                         "2- Borrow a book\n"
                                         "3- Print my orders\n"
                                         "4- Return a book\n"
                                         "5- Back to main\n"
                                         "6- Exit\n")

                    if not my_utils.empty_checker(client_input) and my_utils.digit_checker(client_input):
                        client_input = int(client_input)

                    if client_input == 1:
                        for item1 in my_auth.book_list:
                            print(item1.get_books_info())
                        my_auth.gap_line()

                    elif client_input == 2:
                        order_id = my_auth.get_last_order_id() + 1
                        book_id = input("Enter the book id: ")
                        date = input("Enter the date: ")
                        client_id = id_input
                        status = Constants.ACTIVE
                        if not my_utils.empty_checker(date, book_id) and my_utils.digit_checker(book_id):
                            book_id = int(book_id)
                            if my_auth.is_book_active(book_id=book_id, book_list=my_auth.book_list):
                                my_auth.orders_list.append(
                                        BorrowingOrder(order_id=order_id, date=date,
                                                       client_id=client_id, book_id=book_id,
                                                       status=status))
                                print("Done.")
                                my_auth.gap_line()
                            else:
                                print("Error")

                        else:
                            print("Error, empty value!")

                    elif client_input == 3:
                        is_order_exist = False
                        for item1 in my_auth.orders_list:
                            if item1.get_client_id() == id_input:
                                is_order_exist = True
                                print(item1.get_info_for_orders())
                        if not is_order_exist:
                            print("You do not have any orders!")
                            my_auth.gap_line()
                        my_auth.gap_line()

                    elif client_input == 4:
                        condition = False
                        order_id = input("Order id: ")

                        if not my_utils.empty_checker(order_id) and my_utils.digit_checker(order_id):
                            order_id = int(order_id)

                            for item12 in my_auth.orders_list:
                                if item12.get_id() == order_id and item12.get_client_id() == id_input and item12.get_status() == Constants.ACTIVE:
                                    condition = True
                                    break

                            if condition:
                                my_auth.return_books(order_id=order_id, client_list=my_auth.clients_list,
                                                     order_list=my_auth.orders_list, client_id=id_input,
                                                     book_list=my_auth.book_list)

                                print("Done")
                                my_auth.gap_line()
                            else:
                                print("Access Denied")
                                my_auth.gap_line()
                        else:
                            print("Error")
                            my_auth.gap_line()

                    elif client_input == 5:
                        print("See you :)")
                        my_auth.gap_line()
                        user_condition = False

                    elif client_input == 6:
                        print("Don't leave me alone :(")
                        user_condition = False
                        first_con = False

                    else:
                        print("wrong choice")
                        my_auth.gap_line()

        if not is_id_exist:
            print("This ID does not exist")
            my_auth.gap_line()

