#クラス定義
class Student:
    def __init__(self,name,scores):  #コンストラクタ(名前，成績｛教科・点数｝)
        self.name = name             #変数に記録
        self.scores=scores

    def show_score(self):            #表示
        print(f"名前:{self.name}")
    
        for subject,  score in self.scores.items():
            print(f"{subject}:{score}") 

        print(f"平均値:{self.average():.1f}")

        print(f"成績:{self.rank()}")
    

    def average(self):                #平均値を算出
        return sum(self.scores.values())/len(self.scores)
    
    def rank(self):                   #平均値をランク付けする
        avg = self.average()
        if avg >=90:
            return "S"
        elif avg >=80:
            return "A"
        elif avg >=70:
            return "B"
        elif avg >=60:
            return "C"
        elif avg >=0:
            return "D"


#テストデータ
students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]



#データ表示
print("===学生成績一覧===")
for student_sel in students:
    print(f"名前 : {student_sel.name:<10}平均値 : {student_sel.average():.1f}      成績 : {student_sel.rank()}\n")



#検索処理

while True:
    name_input = input("成績を表示したい学生の名前を入力してください（終了するには'exit'と入力）:")
    print()
    if name_input == "exit":
        print("プログラムを終了します")
        break                         # プログラムを終了

    found = False ###
    for student in students:
        if student.name == name_input:
            student.show_score()      # 名前が見つかった場合、成績を表示
            found = True
            exit()
            break                     # 名前が見つかったらループを抜ける   ###

    if not found:
        print(f"{name_input}は見つかりませんでした") # 名前が見つからなかった場合、再度入力を促す
        print()                             
        print("再度名前を入力してください。")
