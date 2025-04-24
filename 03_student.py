# Studentクラスを定義
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # 例: {"math": 90, "english": 80}

    def average(self):
        return sum(self.scores.values()) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "S"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

    def show_detail(self):
        detail = f"名前：{self.name}\n"
        for subject, score in self.scores.items():
            detail += f"{subject}: {score}\n"
        detail += f"平均点：{self.average():.2f}\n"
        detail += f"成績：{self.grade()}\n"
        return detail

# 複数の学生の成績を一覧表示する関数
def show_all_students(student_list):
    print("=== 学生成績一覧 ===")
    for student in student_list:
        print(f"名前：{student.name} / 平均点：{student.average():.2f} / 成績：{student.grade()}")
    print()

# 学生を名前で検索して詳細を表示する関数
def search_student_by_name(student_list, name):
    for student in student_list:
        if student.name.lower() == name.lower():
            print("=== 成績詳細 ===")
            print(student.show_detail())
            return
    print(f"{name} は見つかりませんでした。\n")

# === テスト用データ ===
students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]

# === 処理 ===
show_all_students(students)

# 繰り返し検索
while True:
    name = input("成績を表示したい学生の名前を入力してください（終了するには 'exit' と入力）：")
    if name.lower() == 'exit':
        print("プログラムを終了します。")
        break
    search_student_by_name(students, name)
