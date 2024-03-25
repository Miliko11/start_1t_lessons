class Person:
    subject = 'Гражданин'

    def __init__(self, name='неизвестное имя', age=None):
        self.name = name
        self.age = age

    def info(self):
        pass

    def say(self, massage):
        print(self.name, 'Говорит:', massage)

    def sing(self):
        print(self.name, 'Поет!')

    def go(self, speed):
        print(self.name, 'Идет со скоростью', speed, 'км/ч')
        if speed < 5:
            self.sing()

    @classmethod
    def big_say(cls):
        print('Говорю громко!')

anna = Person('Анна', 15)
gleb = Person('Глеб', 14)
alex = Person(age=17, name='Алексей')

print(anna.name)
print(alex.age)
print(anna.subject)

men = Person('Миша', 30)


men.go(3)
anna.say('Привет друзья!')