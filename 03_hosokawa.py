import statistics
import math

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores=scores

    def get_average(self):
        return sum(self.scores.values()) / len(self.scores)
    
    def get_grade(self):
        if self.get_average()>90:
            self.grade="S"
        elif self.get_average()>80:
            self.grade="A"
        elif self.get_average()>70:
            self.grade="B"
        else:
            self.grade="C"

        return self.grade


students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]

print("===学生成績一覧===")
for student in students:
    print(f"名前：{student.name}／平均点：{student.get_average():.2f}／成績：{student.get_grade()}")

print("成績を表示したい学生の名前を入力してください（終了するには 'exit' と入力）：")
name=input()
print("===学生成績一覧===")
for student in students:
    if student.name==name: ###
        print(f"名前:{student.name}")
        for subject,score in student.scores.items():
            print(f"{subject}:{score}")
        print(f"平均点：{student.get_average():.2f}")
        print(f"成績：{student.get_grade()}")
        break
    elif name==exit:   ###
        break
    else :
        print(f"{name}は見つかりませんでした．")
        break