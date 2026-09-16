"""student-notes giriş noktası."""

from students import add_student, list_students


def main():
    add_student("Ada Lovelace", 101)
    add_student("Alan Turing", 102)
    add_student("Grace Hopper", 103)

    for student in list_students():
        print(student)


if __name__ == "__main__":
    main()
