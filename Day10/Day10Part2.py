from typing import Dict

with open("Day10Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')
input_numbers_list = [int(i) for i in input_list]
input_numbers_list.append((max(input_numbers_list) + 3))
input_numbers_set = set(input_numbers_list)
set_sorted = sorted(input_numbers_set)


def calculate_numbers(input_set):
    possible_arrangements_dictionary = {0: 1}
    for number in sorted(input_set):
        possible_arrangements_dictionary[number] = 0
        if number - 1 in possible_arrangements_dictionary:
            possible_arrangements_dictionary[number] += possible_arrangements_dictionary[number - 1]
        if number - 2 in possible_arrangements_dictionary:
            possible_arrangements_dictionary[number] += possible_arrangements_dictionary[number - 2]
        if number - 3 in possible_arrangements_dictionary:
            possible_arrangements_dictionary[number] += possible_arrangements_dictionary[number - 3]
    return possible_arrangements_dictionary[max(input_set)]


print(calculate_numbers(set_sorted))
