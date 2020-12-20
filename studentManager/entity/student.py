class Student(object):
    def __init__(self):
        self.student_id = ""
        self.name = ""
        self.sex = ""
        self.age = ""
        self.native_place = ""
        self.student_class = ""
        self.score = ""

    def get_score(self) -> float:
        return float(self.score)