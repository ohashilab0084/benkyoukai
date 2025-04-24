class Student:
    def __init__(self,student_name, student_score):
        self.student_name = student_name
        self.student_score = student_score

    #平均点を計算する
    def average(self):
        return sum(self.student_score.values()) / len(self.student_score)

    #成績を計算する
    def grade(self):
        average = self.average()
        if average >= 90:
            return "S"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        else:
            return "D"
            
#学生成績一覧表示
def all_student(students):
    print("\n=========学生成績一覧=========")
    for student in students:
        print(f"名前：{student.student_name} / 平均点：{student.average():.2f} / 成績：{student.grade()}") 
    print("==============================")

#学生成績詳細
def search_student(students, name):
    for student in students:
        if student.student_name.lower() == name.lower(): ###
            print(f"\n===成績詳細===")
            print(f"名前:{student.student_name}")
            print(f"math:{student.student_score['math']}") ###
            print(f"english:{student.student_score['english']}")
            print(f"science:{student.student_score['science']}")
            print(f"平均点:{student.average():.2f}")
            print(f"成績:{student.grade()}")
            print("==============")
            return
    print(f"\n{name.lower()}は見つかりませんでした.")

#テストデータ
students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]

all_student(students)

while True:
    name = input("\n成績を表示したい学生の名前を入力してください（終了するには 'exit' と入力）: ")
    if name.lower() == "exit": ###
        print("プログラムを終了します.")
        break
    search_student(students, name)

