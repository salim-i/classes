class Animal:
    area = 'Ферма Дядюшки Джо'
    voice = 'Голос'
    animal_type = None

    def set_animal_type(self):
        return self.animal_type


class Milk(Animal):
    animal_type = 'Копытное животное'

    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def get_milk(self):
        print(f'{self.animal_type} по имени {self.name} дает молоко и говорит {self.voice}. ')
        print(f'{self.animal_type} {self.name}: спасибо хозяин {self.voice}! ')

    def get_feed(self):
        print(f'Начинаем кормить {self.animal_type} по имени {self.name}. ')
        print(f'{self.animal_type} {self.name}: спасибо хозяин {self.voice}! ')


class Egg(Animal):
    animal_type = 'Птица'

    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def get_egg(self):
        print(f'{self.animal_type} по имени {self.name} дает яйца и говорит {self.voice}. ')
        print(f'{self.animal_type} {self.name}: спасибо хозяин {self.voice}! ')

    def get_feed(self):
        print(f'Начинаем кормить {self.animal_type} по имени {self.name}. ')
        print(f'{self.animal_type} {self.name}: не голоден, спасибо хозяин {self.voice}! ')


class Wool(Animal):
    animal_type = 'Барашек'

    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def get_wool(self):
        print(f'{self.animal_type} по имени {self.name} дает шерсть и говорит {self.voice}. ')
        print(f'{self.animal_type} {self.name}: спасибо хозяин {self.voice}! ')

    def get_feed(self):
        print(f'Начинаем кормить {self.animal_type} по имени {self.name}. ')
        print(f'{self.animal_type} {self.name}: спасибо хозяин {self.voice}! ')


class Goose(Egg):
    voice = 'Га-га-га'
    animal_type = 'Гусь'


class Cow(Milk):
    voice = 'Му-му-му'
    animal_type = 'Корова'


class Sheep(Wool):
    voice = 'Мэ-мэ-мэ'
    animal_type = 'Овца'


class Chicken(Egg):
    voice = 'Ко-ко-ко'
    animal_type = 'Курица'

    def get_feed(self):
        print(f'Начинаем кормить {self.animal_type} по имени {self.name}. ')
        print(f'{self.animal_type} {self.name}: спасибо хозяин {self.voice}! ')


class Goat(Milk):
    voice = 'Бэ-бэ-бэ'
    animal_type = 'Коза'

    def get_feed(self):
        print(f'Начинаем кормить {self.animal_type} по имени {self.name}. ')
        print(f'{self.animal_type} {self.name}: не голоден, спасибо хозяин {self.voice}! ')


class Duck(Egg):
    voice = 'Кря-кря-кря'
    animal_type = 'Утка'


goose0 = Goose('Серый', 3)
goose1 = Goose('Белый', 2)
cow = Cow('Манька', 300)
sheep0 = Sheep('Барашек', 90)
sheep1 = Sheep('Кудрявый', 100)
chicken0 = Chicken('Ко-Ко', 2)
chicken1 = Chicken('Кукареку', 3)
goat0 = Goat('Рога', 50)
goat1 = Goat('Копыта', 65)
duck = Duck('Кряква', 4)

animals_list = [goose0, goose1, cow, sheep0, sheep1, chicken0, chicken1, goat0, goat1, duck]
print('---------------')
print('Мы приехали помогать на ферму Дядюшки Джо и видим вокруг себя множество разных животных: ')
print('---------------')
for animal in animals_list:
    print(f'{animal.animal_type} по имени {animal.name}')
print()
print('---------------')
print(f'Раз уж мы приехали помогать, за всеми животными нужно ухаживать: корову и коз подоить, овец постричь, собрать яйца у кур, утки и гусей. ')
print('---------------')
for animal in animals_list:
    print()
    print(f'Начинаем собирать яйца у {goose0.animal_type} {goose0.name}, {goose1.animal_type} {goose1.name}, {chicken0.animal_type} {chicken0.name}, {chicken1.animal_type} {chicken1.name}, {duck.animal_type} {duck.name}.')
    print()
    goose0.get_egg()
    print()
    goose1.get_egg()
    print()
    chicken0.get_egg()
    print()
    chicken1.get_egg()
    print()
    duck.get_egg()
    print('---------------')
    break

for animal in animals_list:
    print()
    print(f'Начинаем доить молоко у {cow.animal_type} {cow.name}, {goat0.animal_type} {goat0.name}, {goat1.animal_type} {goat1.name}.')
    print()
    cow.get_milk()
    print()
    goat0.get_milk()
    print()
    goat1.get_milk()
    print('---------------')
    break

for animal in animals_list:
    print()
    print(f'Начинаем стричь шерсть у {sheep0.animal_type} {sheep0.name}, {sheep1.animal_type} {sheep1.name}.')
    print()
    sheep0.get_wool()
    print()
    sheep1.get_wool()
    print('---------------')
    break

print(f'Теперь всех животных нужно покормить: ')
print('---------------')
for animal in animals_list:
    print()
    print(f'Начинаем кормить {goose0.animal_type} {goose0.name}, {goose1.animal_type} {goose1.name}, {chicken0.animal_type} {chicken0.name}, {chicken1.animal_type} {chicken1.name}, {duck.animal_type} {duck.name}.')
    print()
    goose0.get_feed()
    print()
    goose1.get_feed()
    print()
    chicken0.get_feed()
    print()
    chicken1.get_feed()
    print()
    duck.get_feed()
    print('---------------')
    break

for animal in animals_list:
    print()
    print(f'Начинаем кормить {cow.animal_type} {cow.name}, {goat0.animal_type} {goat0.name}, {goat1.animal_type} {goat1.name}.')
    print()
    cow.get_feed()
    print()
    goat0.get_feed()
    print()
    goat1.get_feed()
    print('---------------')
    break

for animal in animals_list:
    print()
    print(f'Начинаем кормить {sheep0.animal_type} {sheep0.name}, {sheep1.animal_type} {sheep1.name}.')
    print()
    sheep0.get_feed()
    print()
    sheep1.get_feed()
    print('---------------')
    break

print()

total_weight = 0
for animal in animals_list:
    total_weight += animal.weight
print(f'Общий вес всех животных на ферме составляет {total_weight} кг.')

print()
max_weight = max(animals_list, key=lambda x: x.weight)
print(f"Самое тяжелое животное на ферме {max_weight.animal_type} по имени {max_weight.name}. Ее вес составляет {max_weight.weight} кг.")

