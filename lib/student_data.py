class student_data:
    def __init__(self, name, age, school, gender, info = '특이사항 없음'):
        self.name = name
        self.age = age
        self.school = school
        self.gender = gender
        self.info = info
        
    def show(self):
        print("name : {}".format(self.name))
        print("age : {}".format(self.age))
        print("school : {}".format(self.school))
        print("gender : {}".format(self.gender))
        print("info : {}".format(self.info))