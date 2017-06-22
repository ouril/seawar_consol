from fun import *
from random import randint, choice

class Field:
    '''Основной класс игры содержащий поле, корабли и метод shot - стрельбу
    '''
    def __init__(self, name='user'):
        self.name = name
        self.filds = tuple(generator_f())
        self.ships = []
        self.shots = []

    def show(self, auto=False):
        '''Показывает поле c караблями если без аргументов и без кораблей с
        '''
        print('\nThe Field of: '+ str(self.name) + '!\n')
        print('\t' + ''.join([' ' +  x + ' ' for x in gen_abc()]) + '\n')
        prin_str = []
        arr = 0
        for i in self.filds:
            if i in self.ships and i in self.shots:
                prin_str += ['X_|']
            elif i in self.ships and not auto:
                prin_str += ['[]|']
            elif i in self.shots:
                prin_str += ['*_|']
            else:
                prin_str += ['__|']
        ind = 0
        #print(prin_str)
        for i in range(1, 11):
            nex = ind + 10
            stri = ''.join(prin_str[ind:nex])
            print(str(i) + '\t' + stri)
            ind += 10

    def random_ship(self):
        """Заполняет поле кораблями рендомно
        """
        list_ship = [4,3,3,2,2,2,1,1,1,1]

        for i in list_ship:
            n = i
            ran = []
            while ran in self.ships or not ran:
                posi = choice([0,1])
                if posi:
                    strok = randint(1, 11 - n)
                    ver = choice(gen_abc())
                    ran = [ver + str(i) for i in range(strok, strok + n)]

                else:
                    strok = randint(1, 11 - n)
                    ver = str(randint(1, 10))
                    ran = [gen_abc(11)[m] + ver for m in range(strok, strok + n)]
                self.ships += ran

    def shot(self, target):
        pass


a = Field()
a.random_ship()
print(a.ships)

a.show()
