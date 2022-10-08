from model.user_db.Person import Person


class Client(Person):

    def __init__(self, client_id, client_phone, name, age, id_no):
        # self.__id = client_id
        self.__client_phone = client_phone
        super(Client, self).__init__(client_id, name, age, id_no)

    def get_clients_info(self):
        return f"Client id: {self.get_id()}, name: {self.get_name()}, age: {self.get_age()}," \
               f" phone: {self.__client_phone}, national id: {self.get_id_no()}"

    def get_client_and_order(self):
        return f"Client id: {self.get_id()}, name: {self.get_name()}"

