class Student:
    def __init__(self, name,scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores.values())/len(self.scores)
    
    def grade(self):
        ave = self.average()
        if ave >= 90:
            return "S"
        elif ave >= 80:
            return "A"
        elif ave >= 70:
            return "B"
        elif ave >= 60:
            return "C"
        else:
            return "D"
    
    def show_student(self):
        print("===成績詳細===")
        print(f"名前 : {self.name}")
        for subject, score in self.scores.items():
            print(f"{subject} : {score}")
        print(f"平均点 : {self.average():.2f}\n成績 : {self.grade()}")

def show_allstudents(students):
    print("===学生成績一覧===")
    for student in students:
        print(f"名前 : {student.name}/ 平均点 : {student.average():.2f}/ 成績 : {student.grade()}")

def search_student(name, student_dict):
    if name in student_dict:
        student_dict[name].show_student()
    else:
        print(f"{name}は見つかりませんでした。")
    
students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]

student_dict = {student.name: student for student in students} ###

show_allstudents(students)

while True:
    name = input("成績を表示したい学生の名前を入力してください(終了するには'exit'と入力) : ")
    if name == 'exit':
        print("プログラムを終了します。")
        break
    search_student(name, student_dict)