import random
import math

level = 1
col = 5
row = 4
data = [['O', '0'], ['I', '1'], ['U', 'V']]
alph = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}


def start_message():
    print('Input cell number (e.g. A1) of the different character.')


def section_message():
    print('Level: ' + str(level))


def view_question():
    choice_int = random.randint(0, 2)
    mistake_number = random.randint(0, 19)
    print('Debug: mistake_number = ' + str(mistake_number))
    print(data[choice_int])
    str_1 = '/|'
    str_2 = '--'
    for x, y in alph.items():
        str_1 += x
    for x in alph:
        str_2 += '-'
    print(str_1)
    print(str_2)
    i = 0
    while i < row:
        j = 0
        output = ''
        while j < col:
            if i * 5 + j == mistake_number:
                output += data[choice_int][1]
            else:
                output += data[choice_int][0]
            j += 1
        print(str(i + 1) + '|' + output)
        i += 1
    return mistake_number


def change_input_number(input_str):
    col_input = alph[input_str[0]] - 1
    row_input = int(input_str[1]) - 1
    input_number = row_input * 5 + col_input
    return input_number


def is_correct_number(mistake_number, input_number):
    if mistake_number == input_number:
        return True
    else:
        return False


def change_string(number):
    col_num = number % col + 1
    row_num = math.floor(number / col) + 1
    string = ''
    for x, y in alph.items():
        if y == col_num:
            string += x
    string += str(row_num)
    return string


def view_result(is_correct, mistake_number):
    if is_correct:
        print('Correct!')
    else:
        print('Wrong')
        print('Correct answer is ' + change_string(mistake_number))


def play():
    start_message()
    section_message()
    choice = input('(e.g. A1)')
    mistake_number = view_question()
    input_number = change_input_number(choice)
    is_correct = is_correct_number(mistake_number, input_number)
    print('Debug:choice = ' + choice)
    print('Debug: input_number = ' + str(change_input_number(choice)))
    view_result(is_correct, mistake_number)


play()
