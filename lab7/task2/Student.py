class Student():
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    
    def add_grade(self, grade):
        self.grades.append(grade)
        return
    
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        else:
            cnt = sum(self.grades)
            return cnt/len(self.grades)
    
    def get_letter_grade(self):
        x = self.get_average()
        if x >= 90 and x <= 100:
            return "A"
        elif x >= 80 and x <= 89:
            return "B"
        elif x >= 70 and x <= 79:
            return "C"
        elif x >= 60 and x <= 69:
            return "D"
        else:
            return "F"
    
    def __str__(self):
        return f"{self.name} ({self.student_id}) - Average: {self.get_average()} ({self.get_letter_grade()})"
    

