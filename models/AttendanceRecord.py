class AttendanceRecord:
    def __init__(self, course_title, attendance_date, start_time, end_time, check_in_time, check_out_time, status):
        self._course_title = course_title
        self._attendance_date = attendance_date
        self._start_time = start_time
        self._end_time = end_time
        self._check_in_time = check_in_time
        self._check_out_time = check_out_time
        self._status = status

    def get_course_title(self):
        return self._course_title

    def get_attendance_date(self):
        return self._attendance_date

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def get_check_in_time(self):
        return self._check_in_time

    def get_check_out_time(self):
        return self._check_out_time

    def get_status(self):
        return self._status

    # Setter methods
    def set_course_title(self, course_title):
        self._course_title = course_title

    def set_attendance_date(self, attendance_date):
        self._attendance_date = attendance_date

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def set_check_in_time(self, check_in_time):
        self._check_in_time = check_in_time

    def set_check_out_time(self, check_out_time):
        self._check_out_time = check_out_time

    def set_status(self, status):
        self._status = status

    # Optional: __str__ method to help with debugging
    def __str__(self):
        return (f"{self._course_title} | Date: {self._attendance_date} | "
                f"Start: {self._start_time} - End: {self._end_time} | "
                f"In: {self._check_in_time} - Out: {self._check_out_time} | Status: {self._status}")
