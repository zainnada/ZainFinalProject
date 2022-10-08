class Person:
    def __init__(self, id, name, age, id_no):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__id_no = id_no

    def set_name(self, name):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self) -> str:
        return self.__age

    def set_id_no(self, id_no):
        self.__id_no = id_no

    def get_id_no(self) -> str:
        return self.__id_no

    def get_id(self):
        return self.__id

