import random


def number_input_check(str_input):
        try:
            num_input = list(map(int, str_input))
        except ValueError:
            print('Only integer')
            return False

        if len(num_input) != 4:
            print('Only four digit')
            return False

        if len(set(num_input)) != 4:
            print('Duplication of number is forbidden.')
            return False

        else:
            return num_input


def hit_and_blow(defense_num, attack_num):
    i = hit = blow = 0
    for num in attack_num:
        if defense_num[i] == num:
            hit += 1
        elif num in defense_num:
            blow += 1
        i += 1

    print('{} HIT!'.format(hit))
    print('{} BLOW!'.format(blow))

    return hit, blow


def practice_mode():
    answer = random.sample([i for i in range(1, 10)], 4)
    print(answer)
    while True:

        print('''please input 4 unique integers, or 'end':''')
        str_input = input()
        if str_input == 'end':
            exit()

        if not number_input_check(str_input):
            continue

        num_input = map(int, str_input)

        hit, blow = hit_and_blow(answer, num_input)

#        i = hit = blow = 0
#        for num in num_input:
#            if answer[i] == num:
#                hit += 1
#            elif num in answer:
#                blow += 1
#
#            i += 1
#        print('{} HIT!'.format(hit))
#        print('{} BLOW!'.format(blow))

        if hit == 4:
            print('You win!')
            exit()


def vscom_mode():
    while True:
        print('Input your 4 numbers')
        str_input = input()

        if not number_input_check(str_input):
            continue

        user_defense = list(map(int, str_input))
        break

    enemy_defense = random.sample([i for i in range(1, 10)], 4)
    print(enemy_defense)
    while True:
        print('Input attack number')
        str_input = input()

        if not number_input_check(str_input):
            continue
        user_attack = map(int, str_input)

        print('Your attack!')
        user_hit, user_blow = hit_and_blow(enemy_defense, user_attack)
        if user_hit == 4:
            print('You Win!')
            exit()

        print('Enemy attack!')
        enemy_attack = random.sample([i for i in range(1, 10)], 4)
        print(enemy_attack)

        enemy_hit, enemy_blow = hit_and_blow(user_defense, enemy_attack)
        if enemy_hit == 4:
            print('You Lose...')


def comcom_mode():
    com1_defense = random.sample([i for i in range(1, 10)], 4)
    print('com1:{}'.format(com1_defense))
    com2_defense = random.sample([i for i in range(1, 10)], 4)
    print('com2:{}'.format(com2_defense))

    print('Com1 attack!')
    com1_hit, com1_blow = hit_and_blow(com1_defense, user_attack)
    if user_hit == 4:
        print('You Win!')
        exit()

    print('Enemy attack!')
    enemy_attack = random.sample([i for i in range(1, 10)], 4)
    print(enemy_attack)

    enemy_hit, enemy_blow = hit_and_blow(user_defense, enemy_attack)
    if enemy_hit == 4:
        print('You Lose...')



while True:
    print('Choose Mode: 1:Your practice 2:You vs Com 3:Com vs Com')
    try:
        game_mode = int(input())
    except ValueError:
        print('Invalid mode')
        continue

    if game_mode == 1:
        practice_mode()

    if game_mode == 2:
        vscom_mode()

    if game_mode == 3:
        practice_mode()

    else:
        print('Invalid mode')
        continue
