class Datas:
    def __init__(self):
        self.arr = []
        self.keys = []
        self.arr_def = []
        self.keys_def = []
        self.print_title = 'Datas'

        for i in range(10):
            self.arr_def.append(i)
            self.keys_def.append(f'data{i + 1}')

        self.print_key, self.print_value = self.keys_def, self.arr_def

    def info(self):
        print(f'\n{self.print_title}:')
        for i in range(len(self.print_key)):
            print(f'{self.print_key[i]}: {self.print_value[i]}')

    def replace(self, index=999):
        try:
            self.arr[index] = input(f'Введите новые данные ({self.keys[index]}): ')
        except IndexError:
            for i in range(len(self.arr)):
                self.arr[i] = input(f'Введите новые данные ({self.keys[i]}): ')


class Cars(Datas):
    def __init__(self, *args):
        Datas.__init__(self)

        for i in args:
            self.arr.append(i)

        self.keys = ['модель', 'год выпуска', 'производитель',
                     'объём двигателя', 'цвет', 'стоимость']

        self.print_title = 'Данные о автомобиле'
        self.print_key, self.print_value = self.keys, self.arr


class Books(Datas):
    def __init__(self, *args):
        Datas.__init__(self)

        for i in args:
            self.arr.append(i)

        self.keys = ['название', 'год выпуска', 'издатель',
                     'жанр', 'автор', 'стоимость']

        self.print_title = 'Данные о книге'
        self.print_key, self.print_value = self.keys, self.arr


class Stadiums(Datas):
    def __init__(self, *args):
        Datas.__init__(self)

        for i in args:
            self.arr.append(i)

        self.keys = ['название', 'год открытия', 'страна',
                     'город', 'вместимость']

        self.print_title = 'Данные о стадионе'
        self.print_key, self.print_value = self.keys, self.arr


car = Cars('Camry', 2008, 'Toyota', 1.8, 'Black', 500000)
car.info()
car.replace(4)
car.info()

book = Books('Преступление и наказание', 2020, 'ACT', 'Роман', 'Фёдор достоевский', 499)
book.info()
book.replace(1)
book.replace(2)
book.info()

stadium = Stadiums('Лужники', 1956, 'Россия', 'Москва', 76880)
stadium.info()
stadium.replace()
stadium.info()
