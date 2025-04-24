#閾値指定
ranks = {"S": 90, "A": 80, "B": 70, "C": 60}

#Studentクラス
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.math = score["math"] ###
        self.english = score["english"]
        self.science = score["science"]
    
    def average(self):
        return (self.math + self.english + self.science)/3
    
    def rank(self):
        if self.average() >= ranks["S"]:
            return 'S'
        elif self.average() >= ranks["A"]:
            return 'A'
        elif self.average() >= ranks["C"]: ###
            return 'B'
        elif self.average() >= ranks["D"]:
            return 'C'
        else:
            return 'D'
    
    def printShort(self):
        print('名前：'+str(self.name)+' / 平均点：'+'{:.2f}'.format(self.average())+' / 成績：'+str(self.rank()))

    def show(self):
        print('===成績詳細===')
        print('名前：'+str(self.name))
        print('math：'+str(self.math))
        print('english：'+str(self.english))
        print('science：'+str(self.science))
        print('平均点：'+'{:.2f}'.format(self.average()))
        print('成績：'+str(self.rank()))

#名前検索関数
def serchName(name):
    for student in students:
        if student.name == name:
            return student

#データ
students = [
    Student("Tanaka", {"math": 85, "english": 90, "science": 78}),
    Student("Suzuki", {"math": 72, "english": 65, "science": 70}),
    Student("Yamada", {"math": 95, "english": 98, "science": 92}),
    Student("Sato", {"math": 60, "english": 58, "science": 63}),
    Student("Kobayashi", {"math": 88, "english": 85, "science": 82})
]

#一覧表示
def showAll():
    print('===学生成績一覧===')
    for student in students:
        student.printShort()
    print()

#データ追加
def inputData():
    name = input('追加する学生の名前を入力してください:')
    math = input('数学のスコアを入力してくださいを入力してください:')
    english = input('英語のスコアを入力してくださいを入力してください:')
    science = input('科学のスコアを入力してくださいを入力してください:')
    students.append(Student(name, {"math": int(math), "english": int(english), "science": int(science)}))

#データ削除
def deleteData():
    name = input('削除する学生の名前を入力してください:')
    try:
        students.remove(serchName(name))
    except:
        print(str(name)+'は見つかりませんでした。')

#メイン処理ーーーーーーー

showAll()
#詳細表示ループ
while(True):
    name = input('成績を表示したい学生の名前を入力してください（終了するにはexitと入力):')
    if name == 'exit':
        exit()
    elif name == 'all':
        showAll()
    elif name == 'add':
        inputData()
        showAll()
    elif name == 'delete':
        deleteData()
        showAll()
    else:
        try:
            serchName(name).show()
        except:
            print(str(name)+'は見つかりませんでした。')
        print()
