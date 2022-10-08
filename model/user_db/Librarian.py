from model.user_db.Person import Person


class Librarian(Person):

    def __init__(self, libr_id, employment_type, name, age, id_no):

        self.__employment_type = employment_type
        super(Librarian, self).__init__(id=libr_id, name=name, age=age, id_no=id_no)

    def get_lib_name(self, id) -> str:
        for item in self.get_id():
            if item == id:
                return self.get_name()

##
