# # import random
# # from random import randint
#
# class Student:
#     #print("Класс Студент")
#     col=0 # атрибут класса (Глобально)
#     def __init__(self, height=160, name=None,age=None):
#         self.height=height
#         self.name=name
#         self.age=age
#         #print(self)
#         #print("Z")
#         Student.col+=1
#     def grow(self,height=5):
#         self.height+=height
#
#     def __str__(self):
#         return f"Меня зовут {self.name} \nМне {self.age} лет"
#
# student1=Student(height=170 ,name="БОГдан", age=13)
# print(student1.__str__())
# #print(student1.name,"рост",student1.height)
# print("Количество студентов",student1.col)
# student1.grow(height=5)
# print(student1.height)
# student2=Student(height=170, name="Крутой чел", age=14)
# print(student2.__str__())
# #print( student2.name,"рост", student2.height)
# print("Количество студентов",student2.col)
# student2.grow(height=15)
# print(student2.height)






from random import randint
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=50
        self.progress=0
        self.live=True

    def study(self):
        print("Время учиться")
        self.happy-=10
        self.progress+=5
    def sleep(self):
        print("Время сна")
        self.happy+=5
    def rest(self):
        print("Время оттдыха")
        self.happy+=10
        self.progress-=5
    def isLive(self):
        if self.happy<=0:
            print("Депресия")
            self.live=False
        if self.progress>=20:
            print("Сессия сдана. \nЕсть больше времени для отдыха")
            self.happy+=15
            self.live=True
        if self.progress<-5:
            print("Сессия не сдана. Ты отчислен!")
            self.live=False
    def day(self):
        print("Уровень счастя: ", self.happy)
        print("Успеваемость в учебе: ", self.progress)

    def choice(self,numDay):
        print("")
        numDay="День №"+str(numDay)+" из жизни студнета "+self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,3)
        if rnd==1: self.study()
        elif rnd == 2: self.sleep()
        else: self.rest()
        self.day()
        self.isLive()

student1 = Student(name="Анатолий")
for i in range(1,8):
    student1.choice(i)
