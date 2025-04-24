class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"名前: {self.name}"

    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def get_rank(self, student_average, overall_average):
        difference = student_average - overall_average
        if difference > 10:
            return "S"
        elif difference > 5:
            return "A"
        elif difference < -5: ###
            return "C"
        elif difference < -10:
            return "D"
        else:
            return "B"

students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]

average_grades = []
for student in students:
    average_grades.append(student.average_grade())

overall_average = sum(average_grades) / len(average_grades)

print("===学生成績一覧===")
for student in students:
    print(f"{student}/ 平均点：{student.average_grade():.2f}/ 成績：{student.get_rank(student.average_grade(), overall_average)}") ###
print("\n")
"""print(f"各生徒の平均点の平均値: {overall_average:.2f}\n")"""

while True:
    search_name = input("成績を表示したい学生の名前を入力してください(終了するには 'exit' と入力): ")
    if search_name == "exit":
        print("プログラムを終了します。")
        break

    target_student = next((student for student in students if student.name == search_name), None) #students リストの中から、student.name が search_name と一致する student を探す
    ###

    if target_student:
        average = target_student.average_grade()
        math_score = target_student.grades.get("math", "データなし") #値を取り出す
        english_score = target_student.grades.get("english", "データなし")
        science_score = target_student.grades.get("science", "データなし")
        rank = target_student.get_rank(average, overall_average)

        print("===成績詳細===")
        print(f"名前：{search_name}")
        print(f"math：{math_score}")
        print(f"english：{english_score}")
        print(f"science：{science_score}")
        print(f"平均点： {average:.2f}")
        print(f"成績：{rank} ")
        print("\n")
    else:
        print(f"{search_name} は見つかりませんでした。\n")










