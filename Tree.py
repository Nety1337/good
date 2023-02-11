from random import randint
class Tree:
    def __init__(self,name):
        self.name=name
        self.visota=0
        self.age=0
        self.live=True
    def poliv(self):
        print("Время попить")
        self.visota+=10
        self.age+=1
    def rest(self):
        print("Время оттдыха")
        self.visota+=10
        self.age+=5
    def magic(self):
        print("магия")
        self.visota-=10
        self.age-=10
    def isLive(self):
        if self.visota<=15:
            print("Ты уже 1,5 метра")
            self.live=False
        if self.age>=20:
            print("стареем")
            self.age+=15
            self.live=True
        if self.visota<-5:
            print("не проросло")
            self.live=False
    def day(self):
        print("Рост: ", self.visota, "м")
        print("Возраст: ", self.age, " лет")
    def choice(self,numDay):
        print("")
        numDay="День №"+str(numDay)+" из жизни дерева по именни "+self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,3)
        if rnd==1:
            self.study()
        elif rnd == 2:
            self.sleep()
        else:
            self.rest()
        self.day()
        self.isLive()

student1 = Tree(name="Анатолий")
for i in range(1, 8):
    student1.choice(i)
