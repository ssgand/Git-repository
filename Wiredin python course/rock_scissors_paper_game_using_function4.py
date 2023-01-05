import random

hands = ['rock', 'scissors', 'paper']

results = {'win': 'you win', 'lose': 'you lose', 'draw': 'draw try again'}


def start_message():
    print('Start "rock-scissors-paper" game')


def is_hand(input):
    if input >= 0 and input <= 2:
        return True
    else:
        return False


def get_player():
    print('Input your hand chose')
    string = input('0=rock, 1=scissors, 2=paper')
    if string == '0' or string == '1' or string == '2':
        hand = int(string)
        return hand
    else:
        return get_player()


def get_computer():
    return random.randint(0, 2)


def view_hand(player, computer):
    print('My hand is', get_hand_name(player))
    print('Computer\'s hand is', get_hand_name(computer))


def get_result(hand_diff):
    if hand_diff == 2 or hand_diff == -1:
        return('win')
    elif hand_diff == 0:
        return('draw')
    else:
        return('lose')


def get_hand_name(hand_number):
    return hands[hand_number]


def view_result(hand_diff):
    print(results[get_result(hand_diff)])


def play():
    your_hand = get_player()
    while not is_hand(your_hand):
        your_hand = get_player()
    computer_hand = get_computer()
    hand_diff = your_hand - computer_hand
    view_hand(your_hand, computer_hand)
    view_result(hand_diff)
    if hand_diff == 0:
        play()


start_message()
play()
