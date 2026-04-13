from Student import Student
from UndergraduateStudent import UnderGraduateStudent
from GraduateStudent import GraduateStudent
from utils import calculate_class_average
from utils import get_students_by_grade
from utils import get_top_student


def main():
    first = GraduateStudent("First", "24V3434", [33,43,54], "Something")
    second = GraduateStudent("Second", "24V34ds4", [90,78,89], "Something")
    third = UnderGraduateStudent("Third", "24V343423", [90,78,89], 2)
    fourth = UnderGraduateStudent("Fourth", "24V3434rer", [90,78,89], 3)
    fifth = UnderGraduateStudent("Fifth", "24V3434dsfa", [78,78,89], 3)


    first.add_grade(3)
    first.add_grade(4)
    first.add_grade(2)

    second.add_grade(3)
    second.add_grade(4)
    second.add_grade(2)

    third.add_grade(3)
    third.add_grade(4)
    third.add_grade(2)

    fourth.add_grade(3)
    fourth.add_grade(4)
    fourth.add_grade(2)

    fifth.add_grade(3)
    fifth.add_grade(4)
    fifth.add_grade(2)

    s = []
    s.append(fifth)
    s.append(first)
    s.append(second)
    s.append(third)
    s.append(fourth)

    for x in range(len(s)):
        print(s[x])


    
    print(calculate_class_average(s))
    get_top_student(s)
    get_students_by_grade(s, "A")


    
    
    for x in range(len(s)):
        print(s[x].get_status())


    






if __name__ == "__main__":
    main()

