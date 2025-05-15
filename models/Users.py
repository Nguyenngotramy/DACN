class Users:
    def __init__(self, id, name, dateofbirth, numphone, password, email):
        self._id = id
        self._name = name
        self._dateofbirth = dateofbirth
        self._numphone = numphone
        self._password = password
        self._email = email

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_dateofbirth(self):
        return self._dateofbirth

    def set_dateofbirth(self, dateofbirth):
        self._dateofbirth = dateofbirth

    def get_numphone(self):
        return self._numphone

    def set_numphone(self, numphone):
        self._numphone = numphone

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
    def get_email(self):
        return self._email

    def set_password(self, email):
        self._email = email
