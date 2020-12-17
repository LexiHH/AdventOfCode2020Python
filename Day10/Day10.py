with open("Day10Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')
input_numbers_list = [int(i) for i in input_list]
input_numbers_list.append(0)
input_numbers_list.append((max(input_numbers_list) + 3))
input_numbers_set = set(input_numbers_list)
set_sorted = sorted(input_numbers_set)


def calculate_differences(sorted_numbers_set):
    count_one_difference = 0
    count_two_difference = 0
    count_three_difference = 0
    for i in range(1, len(sorted_numbers_set)):
        difference = sorted_numbers_set[i] - sorted_numbers_set[i-1]
        if difference == 1:
            count_one_difference += 1
        if difference == 2:
            count_two_difference += 1
        if difference == 3:
            count_three_difference += 1
    return count_one_difference * count_three_difference


print(calculate_differences(set_sorted))




