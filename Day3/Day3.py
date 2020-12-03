with open("Day3Input.txt") as file:
    read_data = file.read()

string_formatted = read_data.split('\n')


def count_trees(string_list, number_along, number_down):
    i = 0
    tree = '#'
    count = 0
    for j in range(0, len(string_list), number_down):
        string_length = len(string_list[j])
        letter = string_list[j][(i % string_length)]
        i += number_along
        if tree in letter:
            count += 1
    return count


def calc_run_multiplication(string_list):
    total = 1
    instructions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for number_along, number_down in instructions:
        trees = count_trees(string_list, number_along, number_down)
        total *= trees
    return total


print(calc_run_multiplication(string_formatted))
