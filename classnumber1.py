class Fruit:
    size = 0

    def __init__(self, name="Фрукт", color="Зеленый", status=False):
        self.name = name
        self.color = color
        self.status = status
        self.__size = 0

    def growth(self):
        print(self.name, 'Растет, растет и вырос!....')
        self.status = True
        self.__size = 100


class Vegetables:
    pass

f1 = Fruit()
#print(f1.name, f1.color, f1.status)
f2 = Fruit(name='Яблоко')
#print(f2.name, f2.color, f2.status)
f3 = Fruit(name='Персик', color='Жёлто-зелёный')
print(f3.name, f3.color, f3.status)
f4 = Fruit(name='Апельсин', color='Оранжевый', status=True)
#print(f4.name, f4.color, f4.status)

f3.growth()
f3.color = 'Розово-Желтый'
print(f3.name, f3.color, f3.status)
