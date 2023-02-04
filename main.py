from random import randint
class cat:
    def __init__(self,name):
        self.name=name
        self.happy=50
        self.dream=100
        self.live=True
    def net(self):
        print("Побили котика :(")
        self.happy-=50
        self.dream-=35
    def play(self):
        print("Время гулять")
        self.happy+=10
        self.dream-=15
    def sleep(self):
        print("Время сна")
        self.happy+=5
    def relax(self):
        print("Время оттдыха")
        self.happy+=10
        self.dream+=15
    def isLive(self):
        if self.happy<=0:
            print("Грустно")
            self.live=False
        if self.dream>=20:
            print("Жывём")
            self.happy+=15
            self.live=True
        if self.dream<=5:
            print("Грусно")
            self.live=False
        # if self.net:
        #     print("Ему болно")
    def day(self):
        print("Уровень счастя: ", self.happy)
        print("Уровень оттдыха: ", self.dream)

    def choice(self,numDay):
        print("")
        numDay="Месяц №"+str(numDay)+" из жизни КОТИКА по именни "+self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,3)
        if rnd==1: self.play()
        elif rnd == 2: self.sleep()
        else: self.play()

        self.day()
        self.isLive()

cat = cat(name="Рижик")
for i in range(1,13):
    cat.choice(i)