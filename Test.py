class opros:
    def __init__(self, vopros):
        self.vopros = vopros
        self.otvet = []
    def __str__(self):
        print(self.vopros)
    def save(self, otv):
        self.otvet.append(otv)
    def rez(self):
        print("Результат опроса:")
        for i in self.otvet:
            print(" -", i)