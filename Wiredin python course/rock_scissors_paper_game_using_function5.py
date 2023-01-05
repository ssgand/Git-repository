import random

hands = ['rock', 'scissors', 'paper']
results = {'win': 'you win', 'lose': 'you lose', 'draw': 'draw try again'}


def start_message():
    print('Start \'rock-scissors-paper\' game')


def is_hand(x):
    if (x.isdigit() == True):
        if int(x) >= 0 and int(x) <= 2:
            return True
        else:
            return False
    else:
        return False


def get_player():
    print('Input your hand choice')
    input_message = ''
    x = 0
    for hand in hands:
        input_message += str(x) + ':' + hand
        if x < 2:
            input_message += ', '
        x += 1
    return input(input_message)


def get_computer():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[int(hand_number)]


def view_hand(player, computer):
    print('My hand is', get_hand_name(player))
    print('Computer\'s hand is', get_hand_name(computer))


def get_result(hand_diff):
    if hand_diff == 0:
        return 'draw'
    elif hand_diff == -1 or hand_diff == 2:
        return 'win'
    else:
        return 'lose'


def view_result(result):
    print(results[result])


def play():
    your_hand = get_player()
    while (True):
        if (is_hand(your_hand) == False):
            your_hand = get_player()
        else:
            break
    computer_hand = get_computer()
    view_hand(your_hand, computer_hand)
    hand_diff = int(your_hand) - computer_hand
    result = get_result(hand_diff)
    view_result(result)
    if hand_diff == 0:
        play()


start_message()

play()
