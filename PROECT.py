class ak:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.tran_his = []

    def dep(self):
        asc="Вы в "+self.name+" положили"+" 50 грн"
        self.balance+=50
        self.tran_his.append(asc)
        print(asc)

    def gen(self):
        abf = "Вы в " + self.name + " сняли" + " 50 грн"
        self.balance -= 50
        self.tran_his.append(abf)
        print(abf)

    def schet(self):
        print("Ваш счет в "+ self.name, ": ", self.balance)

    def his(self):
        print(self.his)


ban1 = ak("MONO", 203)
ban1.schet()
ban1.dep()
ban1.schet()
ban1.gen()
ban1.schet()
ban1.his()

print()

class perevod:
    def __init__(self, name):
        self.name = name

    def trans(self, chis, cur, resp):
        print(f"Выполняется перевод {chis} {cur} на счет {resp}...")

    def bank(self):
        print(f"Доступны следующие мгновенные переводы для {self.name}:")
        print(" - Приват24")
        print(" - Western Union")
        print(" - MoneyGram")

transfer = perevod("польз 1")
transfer.bank()

transfer.trans(100, "USD", "польз 2")