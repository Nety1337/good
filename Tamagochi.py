class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.satiety = 0
        self.mood = 0

    @property
    def mood(self):
        return self.__mood

    @mood.setter
    def mood(self, value):
        self.__mood = self.satiety + value

    def talk(self):
        self.mood += 1
        print(f'{self.name} радостно произнес: Привет!')

    def eat(self):
        self.satiety += 1
        print(f'{self.name} довольно проглотил полезную пищу')

    def play(self):
        self.mood += 1
        print(f'{self.name} весело поиграл и потряс попкой')