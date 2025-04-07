from university.student import Student


class Course:

    def __init__(self, sid: int, title: str, teacher: str) -> None:
        self._sid = sid
        self._title = title
        self._teacher = teacher
        self._students = []

    def get_title(self) -> str:
        return self._title

    def get_teacher(self) -> str:
        return self._teacher
    
    def get_id(self) -> int:
        return self._sid

    def add_student(self, student: Student) -> None:
        # aggiungo studente alla lista studenti
        self._students.append(student)
    
    def get_students(self) -> list[Student]:
        return self._students
    
    def __str__(self) -> str:
        # rappresentazione in stringa del corso
        return "{},{},{}".format(self._sid, self._title, self._teacher)
