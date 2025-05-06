class Users:
  def __init__(self,id ,name, dateofbirth, numphone, password):
    self.id = id
    self.name = name
    self.dateofbirth = dateofbirth
    self.numphone = numphone
    self.password = password

# Getter và Setter cho id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    # Getter và Setter cho name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter và Setter cho age
    def get_dateofbirth(self):
        return self._dateofbirth

    def set_dateofbirth(self, dateofbirth):
        self._dateofbirth = dateofbirth

    # Getter và Setter cho numphone
    def get_numphone(self):
        return self._numphone

    def set_numphone(self, numphone):
        self._numphone = numphone

    # Getter và Setter cho password
    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
