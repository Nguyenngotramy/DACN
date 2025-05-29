from .users import Users

class Teacher(Users):
    def __init__(self, id, name, dateofbirth, numphone, password, email,department):
        super().__init__(id, name, dateofbirth, numphone, password, email)
        self._department = department

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department
