class LessonModel:
    def __init__(self, course_id, course_name, lecture_name, study_date):
        self._course_id = course_id
        self._course_name = course_name
        self._lecture_name = lecture_name
        self._study_date = study_date

    def get_course_id(self):
        return self._course_id

    def set_course_id(self, value):
        self._course_id = value

    def get_course_name(self):
        return self._course_name

    def set_course_name(self, value):
        self._course_name = value

    def get_lecture_name(self):
        return self._lecture_name

    def set_lecture_name(self, value):
        self._lecture_name = value

    def get_study_date(self):
        return self._study_date

    def set_study_date(self, value):
        self._study_date = value

    def __repr__(self):
        return (
            f"LessonModel(course_id='{self._course_id}', "
            f"course_name='{self._course_name}', "
            f"lecture_name='{self._lecture_name}', "
            f"study_date='{self._study_date}')"
        )

    def to_dict(self):
        return {
            "course_id": self._course_id,
            "course_name": self._course_name,
            "lecture_name": self._lecture_name,
            "study_date": self._study_date
        }
