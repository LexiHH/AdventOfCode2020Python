with open("Day5Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')


def calculate_row_number(string):
    number = [0, 127]
    for letter in string:
        midway = (number[0] + number[1] + 1)/2
        if letter == 'F':
            number[1] = midway - 1
        elif letter == 'B':
            number[0] = midway
    return number[0]


def calculate_column_number(string):
    number = [0, 7]
    for letter in string:
        midway = (number[0] + number[1] + 1)/2
        if letter == 'L':
            number[1] = midway - 1
        elif letter == 'R':
            number[0] = midway
    return number[0]


def calculate_seat_id(seat_number):
    row = calculate_row_number(seat_number[0:7])
    column = calculate_column_number(seat_number[7:])
    id = (row * 8) + column
    return id


def calculate_highest_seat_id(seat_list):
    highest_id = 0
    for seat_number in seat_list:
        id = calculate_seat_id(seat_number)
        if id > highest_id:
            highest_id = id
    return highest_id


def find_missing_seat(seat_list):
    id_list = []
    for seat_number in seat_list:
        id_list.append(calculate_seat_id(seat_number))
    id_list.sort()
    for id_number in id_list:
        if (id_number + 1) not in id_list:
            return id_number + 1
    return id_list


print(find_missing_seat(input_list))



