from Student import Student
from UndergraduateStudent import UnderGraduateStudent
from GraduateStudent import GraduateStudent

def calculate_class_average(s):
    sum  = 0
    for x in range(len(s)):
        sum+=s[x].get_average()
    
    return sum/len(s)
    


def get_top_student(s):
    best = 0
    nameBest = ""
    for x in range(len(s)):
        if best < s[x].get_average():
            best = s[x].get_average()
            nameBest = s[x].name
    
    print(nameBest)


def get_students_by_grade(s, letter):
        for x in range(len(s)):
            if s[x].get_letter_grade() == letter:
                print(s[x].name)