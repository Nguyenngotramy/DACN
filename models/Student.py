from .users import Users

class Student(Users):
    def __init__(self, id, name, dateofbirth, numphone, password,email, school_year, homeroom_class, major, faculty):
        super().__init__(id, name, dateofbirth, numphone, password,email)
        self._school_year = school_year
        self._homeroom_class = homeroom_class
        self._major = major
        self._faculty = faculty

    def get_school_year(self):
        return self._school_year

    def get_homeroom_class(self):
        return self._homeroom_class

    def get_major(self):
        return self._major

    def get_faculty(self):
        return self._faculty
