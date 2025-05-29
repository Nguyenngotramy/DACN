class TeachingSchedule:
    def __init__(self,id, course_name, room, weekday, period_count, weeks):
        self._id = id
        self._course_name = course_name
        self._room = room
        self._weekday = weekday
        self._period_count = period_count
        self._weeks = weeks
    def get_id(self):
        return self._id

    def set_course_name(self, id):
        self._id = id

    def get_course_name(self):
        return self._course_name

    def set_course_name(self, course_name):
        self._course_name = course_name

    def get_room(self):
        return self._room

    def set_room(self, room):
        self._room = room

    def get_weekday(self):
        return self._weekday

    def set_weekday(self, weekday):
        self._weekday = weekday

    def get_period_count(self):
        return self._period_count

    def set_period_count(self, period_count):
        self._period_count = period_count

    def get_weeks(self):
        return self._weeks

    def set_weeks(self, weeks):
        self._weeks = weeks
