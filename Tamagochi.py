# class Tamagotchi:
#     def __init__(self, name):
#         self.name = name
#         self.satiety = 0
#         self.mood = 0
#
#     @property
#     def mood(self):
#         return self.__mood
#
#     @mood.setter
#     def mood(self, value):
#         self.__mood = self.satiety + value
#
#     def talk(self):
#         self.mood += 1
#         print(f'{self.name} радостно произнес: Привет!')
#
#     def eat(self):
#         self.satiety += 1
#         print(f'{self.name} довольно проглотил полезную пищу')
#
#     def play(self):
#         self.mood += 1
#         print(f'{self.name} весело поиграл и потряс попкой')

import time

class Tamagotchi:
    def __init__(self, name):
        self._name = name
        self._hunger = 50
        self._happiness = 50
        self._last_update = time.time()

    @property
    def name(self):
        return self._name

    @property
    def hunger(self):
        time_since_last_update = time.time() - self._last_update
        self._hunger -= time_since_last_update / 10
        self._last_update = time.time()
        return self._hunger

    @property
    def happiness(self):
        time_since_last_update = time.time() - self._last_update
        self._happiness -= time_since_last_update / 20
        self._last_update = time.time()
        return self._happiness

    def talk(self):
        self._happiness += 10
        if self._happiness > 100:
            self._happiness = 100
        print(f"{self._name} says: 'Hello!'")

    def eat(self):
        self._hunger += 10
        if self._hunger > 100:
            self._hunger = 100
        print(f"{self._name} eats some food.")

    def play(self):
        self._hunger -= 10
        if self._hunger < 0:
            self._hunger = 0
        self._happiness += 20
        if self._happiness > 100:
            self._happiness = 100
        print(f"{self._name} plays with a toy.")

my_pet = Tamagotchi("Генадий")

print(my_pet.name)
print(my_pet.hunger)
print(my_pet.happiness)
my_pet.talk()
my_pet.eat()
my_pet.play()
