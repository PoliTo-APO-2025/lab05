from university.course import Course
from university.student import Student


class Timeslot:
    def __init__(self, ts_id: int, room: str, day: int, slot_num: int) -> None:
        self._ts_id = ts_id
        self._room = room
        self._day = day
        self._slot_num = slot_num
        self._course = None
        self._students = []

    def get_id(self) -> int:
        return self._ts_id

    def get_room(self) -> str:
        return self._room

    def get_day(self) -> int:
        return self._day

    def get_slot_num(self) -> int:
        return self._slot_num

    def is_booked(self) -> bool:
        return self._course is not None

    def book(self, course: Course) -> None:
        self._course = course

    def get_course(self) -> Course | None:
        return self._course

    def add_student(self, student: Student) -> None:
        self._students.append(student)

    def get_students(self) -> list[Student]:
        return self._students
