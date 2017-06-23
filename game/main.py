from seawar import Field
from fun import ran_field

if __name__ == "__main__":
    user = input("Введите ваше имя:\n>>>")
    player = Field(user)
    ok = ''
    while ok != 'y' or not ok:
        player.random_ship()
        player.show()
        ok = input("Если раскладка устраевает введите 'y'\n>>>")

    comp = Field("computer")
    comp.random_ship()
    print("Начали!!!")
    turn_side = True
    turn = 0
    while not player.islose() or not comp.islose() or turn == 0:
        turn += 1
        if turn_side:
            comp.show(1)
            target = input("Куда стреляем?\n>>>")
            shot = comp.shot(target)
            if shot:
                print("Попал!\n")
                continue
            else:
                print("Мимо!\n")
                turn_side = False
        else:
            player.show()
            shot = player.shot(ran_field())
            if shot:
                print("Попал!\n")
                continue
            else:
                print("Мимо!\n")
                turn_side = True
