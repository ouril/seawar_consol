from random import choice


def next_abc(argv='A'):
    """Функция возвращает следующую букву по алфавиту
    """
    return chr(ord(argv)+1)

def next_abc_r(argv='Z'):
    """Функция возвращает следующую букву по алфавиту в обратном порядке
    """
    return chr(ord(argv)-1)

def gen_abc(arg=10):
    """Функция возвращает буквы по алфавиту по колличеству указанному аргументом
    если аргумент больше числа букв в алфавите - выйдет ValueError
    """
    if arg < 26:
        abc = ['A']
        for i in range(arg-1):
            abc.append(next_abc(abc[i]))
        return abc
    else:
        raise ValueError

def generator_f():
    """Функция   генерирует список с координиатарами для поля
    """
    fild = []
    num = [x for x in range(1, 11)]
    #порядок важен для печати

    for i in gen_abc():
        for a in num:
            fild.append(i + str(a))
    return fild

def ran_field():
    '''Возвращает рендомное поле
    '''
    return choice(generator_f())
