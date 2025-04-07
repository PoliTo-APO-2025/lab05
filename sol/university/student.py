class Student:

    def __init__(self, cid: int, name: str, surname: str) -> None:
        self._cid = cid
        self._name = name
        self._surname = surname
        self._courses = []

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname
    
    def get_id(self) -> int:
        return self._cid

    def add_course(self, course) -> None:
        # aggiungo corso alla lista corsi
        self._courses.append(course)
    
    def get_courses(self) -> list["Course"]:
        return self._courses

    def __str__(self) -> str:
        # rappresentazione in stringa dello studente
        return "{} {} {}".format(self._cid, self._name, self._surname)
