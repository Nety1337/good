class Tree:
    def __init__(self):
        self.isWorking = False
    def work(self):
        self.isWorking = True
    def calling(self):
        if self.isWorking:
            print("Поступил звонок")
    def info(self):
        print("Состояние телефона ", self.isWorking)
class Mobile(Tree):
    def __init__(self):
        super().__init__()
        self.battery=0
    def charge(self, procents):
        self.battery = procents
        print("Заряд батареи:", self.battery, "%")
    def info(self):
        print("Заряд батареи:", self.battery)
def poli():
    for i in Tree, Mobile:
        i().info()
print(poli())

# tel1 = Mobile()
# #tel1.work()
# tel1.calling()
# tel1.charge(59)