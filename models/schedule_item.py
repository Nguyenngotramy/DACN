class ScheduleItem:
    def __init__(self, course_title, lecturer, weeks, room, day_period, course_schedule):
        self._course_title = course_title
        self._lecturer = lecturer
        self._weeks = weeks
        self._room = room
        self._day_period = day_period
    def get_course_title(self):
        return self._course_title

    def get_lecturer(self):
        return self._lecturer

    def get_weeks(self):
        return self._weeks

    def get_room(self):
        return self._room

    def get_day_period(self):
        return self._day_period


    def set_course_title(self, course_title):
        self._course_title = course_title

    def set_lecturer(self, lecturer):
        self._lecturer = lecturer

    def set_weeks(self, weeks):
        self._weeks = weeks

    def set_room(self, room):
        self._room = room

    def set_day_period(self, day_period):
        self._day_period = day_period

