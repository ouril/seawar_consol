from fun import *
from random import randint, choice
from re import compile, search

class Field:
    '''Основной класс игры содержащий поле, корабли и метод shot - стрельбу
    '''
    def __init__(self, name='user'):
        self.name = name
        self.filds = tuple(generator_f())
        self.ships = []
        self.shots = []
        self.near = []

    def show(self, auto=False):
        '''Показывает поле c караблями если без аргументов и без кораблей с
        '''

        prin_str = []
        arr = 0
        for i in self.filds:
            if i in self.ships and i in self.shots:
                prin_str.append('X_|')
            elif i in self.ships and not auto:
                prin_str.append('[]|')
            elif i in self.shots:
                prin_str.append('*_|')
            else:
                prin_str.append('__|')

        ind = 0
        print('\nThe Field of: '+ str(self.name) + '!\n')
        print('\t' + ''.join([' ' +  x + ' ' for x in gen_abc()]) + '\n')
        for i in range(1, 11):
            nex = ind + 10
            stri = ''.join(prin_str[ind:nex])
            print(str(i) + '\t' + stri)
            ind += 10

    def random_ship(self):
        """Заполняет поле кораблями рендомно
        """
        list_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for i in list_ship:
            n = i
            ran = []

            while not ran or any([i in self.near for i in ran]):
                ran = []
                posi = choice([0,1])

                if posi:
                    strok = randint(1, 11 - n)
                    ver = choice(gen_abc())
                    ran = [ver + str(i) for i in range(strok, strok + n)]

                else:
                    strok = randint(1, 11 - n)
                    ver = str(randint(1, 10))
                    ran = [gen_abc(11)[m] + ver for m in range(strok, strok + n)]


            self.ships.extend(ran)

            for a in [big_point(i) for i in ran]:
                self.near.extend(a)


    def shot(self, target):
        '''Метод для стрельбы!
        '''
        point = compile(r'^[A-J][1-9][0]*$')
        if not point.search(target.upper()):
            while not point.search(target.upper()):
                target = input('Ошибка надписи поля!\nВведите цель: \n>>>')
        self.shots.append(target.upper())
        if target.upper() in self.ships:
            return True
        else:
            return False

    def islose(self):
        if all([i in self.ships for i in self.shots]):
            return True
