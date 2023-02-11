from Test import opros
from random import randint

quest = ["Тебе 5 лет?", "Ты лысый?", "Ты в 20 классе?", "Ты из Китая?", "Го в майн?"]
print("\033[31mВведите х для остановки опроса !!!")
while True:
    if not quest:
        print("Вопросов больше нет")
        break
    rdn = randint(0, len(quest)-1)
    myQ = opros(quest[rdn])
    myQ.__str__()
    try:
        answer = input("Введите ответ: ")
    except:
        print("Допущенна ошибка!!!")
    if answer == "x" or answer =="х":
        print("Ладно пока")
        break
    myQ.save(answer)
    del quest[rdn]
print("Спасибо за участие")
myQ.rez()