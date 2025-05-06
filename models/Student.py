from users import Users

class Student(Users):
    def __init__(self, id, name, dateofbirth, numphone, password,school_year,homeroom_class):
        super().__init__(id, name, dateofbirth, numphone, password)
        self._school_year = school_year
        self._homeroom_class = homeroom_class


    def get_school_year(self):
        return self._school_year

    def set_school_year(self, school_year):
        self._school_year = school_year
