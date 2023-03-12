import random

spis = ['k',
        'n',
        'b',
        ]


round = 1
computer_win = 0
human_win = 0


def cv():
    global computer_value
    rand_value = random.randint(0,2)
    computer_value = spis[rand_value]
    nachinka()
def nachinka():
    global round
    global human_win
    global computer_win
    global computer_value
    global human_value
    if human_value == 'k':
        human_value = 'камень'
    elif human_value == 'n':
        human_value = 'ножницы'
    elif human_value == 'b':
        human_value = 'бумага'
    if computer_value == 'k':
        computer_value = 'камень'
    elif computer_value == 'n':
        computer_value = 'ножницы'
    elif computer_value == 'b':
        computer_value = 'бумага'
    print('Твой ход:', human_value.upper(), '|', 'Мой ход:', computer_value.upper())
    if human_value == 'камень' and computer_value == 'камень':
        print('---Ничья.')
        process()
    if human_value == 'камень' and computer_value == 'ножницы':
        round += 1
        human_win += 1
        print('---Поздравляю, ты выиграл!')
        process()
    if human_value == 'камень' and computer_value == 'бумага':
        round += 1
        computer_win += 1
        print('---Ты проиграл...')
        process()
    if human_value == 'ножницы' and computer_value == 'ножницы':
        print('---Ничья.')
        process()
    if human_value == 'ножницы' and computer_value == 'бумага':
        round += 1
        human_win += 1
        print('---Поздравляю, ты выиграл!')
        process()
    if human_value == 'ножницы' and computer_value == 'камень':
        round += 1
        computer_win += 1
        print('---Ты проиграл...')
        process()
    if human_value == 'бумага' and computer_value == 'бумага':
        print('---Ничья.')
        process()
    if human_value == 'бумага' and computer_value == 'камень':
        round += 1
        human_win += 1
        print('---Поздравляю, ты выиграл!')
        process()
    if human_value == 'бумага' and computer_value == 'ножницы':
        round += 1
        computer_win += 1
        print('---Ты проиграл...')
        process()

def process():

    global human_value
    print('СЧЕТ - Игрок:', human_win, 'Компьютер:', computer_win)
    if round == 1:
        prepare = input('Для готовности нажми x ')
        if prepare == 'x':
            print('Раунд:', round)
        else:
            process()
    else:
        print('Раунд:', round)
    human_value = input('Ходи... ')
    if human_value == 'quit':
        print('Жаль, что ты так рано сдался:(((  прощай')
        quit()
    if human_value != 'k' and human_value != 'n' and human_value != 'b':
        print('Мудила, я же внятно объяснил! '
              '"k" - камень, "n" - ножницы, "b" - бумага')
        process()
    cv()
def game():
    print('Добро пожаловать на битву, мой юный друг! '
          'Разминай свои пальчики, и в бой!')
    print('"k" - камень, "n" - ножницы, "b" - бумага')
    process()

game()


