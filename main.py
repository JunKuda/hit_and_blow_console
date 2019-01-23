import random
import itertools


# 受け取った数字が重複のない４桁か？
# 不正な値ならエラーメッセージを出力してFalseを返す
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


# 防御の数字，攻撃の数字を受け取りヒット数とブロー数を返す
def hit_and_blow(defense_num, attack_num):
    i = hit = blow = 0
    for num in attack_num:
        if defense_num[i] == num:
            hit += 1
        elif num in defense_num:
            blow += 1
        i += 1

    return hit, blow


def com_think_number(candidates, before_atk, before_hit, before_blow):
    next_candidates = []
    for candidate_num in candidates:
        hit, blow = hit_and_blow(candidate_num, before_atk)
        if hit == before_hit and blow == before_blow:
            next_candidates.append(candidate_num)

    return next_candidates


def practice_mode():
    answer = random.sample([i for i in range(1, 10)], 4)
    # print(answer)
    while True:

        print('''please input 4 unique integers, or 'end':''')
        str_input = input()
        if str_input == 'end':
            break

        if not number_input_check(str_input):
            continue

        num_input = map(int, str_input)
        hit, blow = hit_and_blow(answer, num_input)

        print('{} HIT!'.format(hit))
        print('{} BLOW!'.format(blow))

        if hit == 4:
            print('You win!')
            break


def vscom_mode():
    while True:
        print('Input your 4 numbers')
        str_input = input()

        if not number_input_check(str_input):
            continue

        user_defense = list(map(int, str_input))
        break

    enemy_defense = random.sample([i for i in range(1, 10)], 4)
    # print(enemy_defense)
    while True:
        print("Input attack number or 'end'")
        str_input = input()

        if str_input == 'end':
            break

        if not number_input_check(str_input):
            continue
        user_attack = map(int, str_input)

        print('Your attack!')
        user_hit, user_blow = hit_and_blow(enemy_defense, user_attack)

        print('{} HIT!'.format(user_hit))
        print('{} BLOW!'.format(user_blow))

        if user_hit == 4:
            print('You Win!')
            exit()

        print('Enemy attack!')
        enemy_attack = random.sample([i for i in range(1, 10)], 4)
        print(enemy_attack)
        enemy_hit, enemy_blow = hit_and_blow(user_defense, enemy_attack)

        print('{} hit!'.format(enemy_hit))
        print('{} BLOW!'.format(enemy_blow))

        if enemy_hit == 4:
            print('You Lose...')


def comcom_mode():
    com1_defense = random.sample([i for i in range(1, 10)], 4)
    print('com1:{}'.format(com1_defense))
    com2_defense = random.sample([i for i in range(1, 10)], 4)
    print('com2:{}'.format(com2_defense))

    cnt = 0
    candidates = list(itertools.permutations(range(1, 10), 4))
    while True:
        cnt += 1
        com1_attack = random.choice(candidates)
        print('Com1 attack!: {}'.format(com1_attack))
        com1_hit, com1_blow = hit_and_blow(com2_defense, com1_attack)

        print('{} HIT!'.format(com1_hit))
        print('{} BLOW!'.format(com1_blow))

        candidates = com_think_number(candidates, com1_attack, com1_hit, com1_blow)
        if com1_hit == 4:
            print('Com1 Win!')
            print('{} times tried'.format(cnt))
            break

        com2_attack = random.sample([i for i in range(1, 10)], 4)
        print('Com2 attack!: {}'.format(com2_attack))
        com2_hit, com2_blow = hit_and_blow(com1_defense, com2_attack)

        print('{} HIT!'.format(com2_hit))
        print('{} BLOW!'.format(com2_blow))

        candidates = com_think_number(candidates, com1_attack, com1_hit, com1_blow)
        if com2_hit == 4:
            print('Com2 Win!')
            print('{} times tried'.format(cnt))
            break


while True:
    print('Choose Mode: 1:Your practice 2:You vs Com 3:Com vs Com 4:End')
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
        comcom_mode()

    if game_mode == 4:
        exit()

    # elseにするとなぜかうまくいかない
    if game_mode not in [1, 2, 3, 4]:
        print('Invalid mode')
        continue
