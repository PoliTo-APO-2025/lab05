from university import University


def main():
    # R1
    print("-------- R1 --------")
    uni = University("PoliTo")
    uni.set_rector("Guido", "Saracco")
    print(uni.get_name())       # PoliTo
    print(uni.get_rector())     # Guido Saracco

    # R2
    print("-------- R2 --------")
    sid_1 = uni.add_student("Mario", "Rossi")
    sid_2 = uni.add_student("Enrico", "Bianchi")
    print(sid_1, sid_2)                 # 10000 10001
    print(uni.get_student_info(sid_1))  # 10000 Mario Rossi
    print(uni.get_student_info(sid_2))  # 10001 Enrico Bianchi

    # R3
    print("-------- R3 --------")
    cid_1 = uni.add_course("Algoritmi e Programmazione a Oggetti", "Filippo Gandino")
    cid_2 = uni.add_course("Informatica", "Filippo Gandino")
    print(cid_1, cid_2)                 # 10 11
    print(uni.get_course_info(cid_1))   # 10,Algoritmi e Programmazione a Oggetti,Filippo Gandino
    print(uni.get_course_info(cid_2))   # 11,Informatica,Filippo Gandino

    # R4
    print("-------- R4 --------")
    uni.register_to_course(sid_1, cid_1)
    uni.register_to_course(sid_2, cid_1)
    uni.register_to_course(sid_1, cid_2)

    print("Partecipanti corso {}:".format(cid_1))       # Partecipanti corso 10:
    print(uni.get_attendees(cid_1))                     # 10000 Mario Rossi
                                                        # 10001 Enrico Bianchi

    print("Partecipanti corso {}:".format(cid_2))       # Partecipanti corso 11:
    print(uni.get_attendees(cid_2))                     # 10000 Mario Rossi

    print("Piano studio studente {}:".format(sid_1))    # Piano studio studente 10000:
    print(uni.get_study_plan(sid_1))                    # ['10,Algoritmi e Programmazione a Oggetti,Filippo Gandino', '11,Informatica,Filippo Gandino']

    print("Piano studio studente {}:".format(sid_2))    # Piano studio studente 10001:
    print(uni.get_study_plan(sid_2))                    # ['10,Algoritmi e Programmazione a Oggetti, Filippo Gandino']

    # R5
    print("-------- R5 --------")
    ts_id_1 = uni.add_timeslot("4T", 1, 5)
    ts_id_2 = uni.add_timeslot("1T", 4, 1)  
    print(ts_id_1)                                  # 1
    print(ts_id_2)                                  # 2

    uni.book_timeslot(ts_id_1, cid_1)
    print(uni.get_course_in_timeslot(ts_id_1))      # 10

    uni.book_timeslot(ts_id_2, cid_1)
    print(uni.get_course_in_timeslot(ts_id_2))      # 10

    uni.attend_in_timeslot(ts_id_1, sid_1)
    uni.attend_in_timeslot(ts_id_1, sid_2)
    print(uni.get_students_in_timeslot(ts_id_1))    # ['Rossi', 'Bianchi']

    uni.attend_in_timeslot(ts_id_2, sid_1)
    print(uni.get_missing_students_in_timeslot(ts_id_2))    # ['Bianchi']


if __name__ == "__main__":
    main()




