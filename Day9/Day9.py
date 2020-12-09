with open("Day9Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')
input_numbers_list = test_list = [int(i) for i in input_list]


def find_invalid_number(input_list, preamble, numbers_considered):
    for i in range(preamble, len(input_list)):
        possible_sums = sum_numbers(input_list[(i-numbers_considered):i])
        if input_list[i] not in possible_sums:
            return input_list[i]


def sum_numbers(numbers_to_sum):
    possible_sums = set()
    for number in numbers_to_sum:
        numbers_to_consider = numbers_to_sum.copy()
        numbers_to_consider.remove(number)
        for each in numbers_to_consider:
            possible_sums.add(number+each)
    return possible_sums


def find_contiguous_numbers(number, input_list):
    for i in range(0, len(input_list)):
        total = input_list[i]
        contiguous_numbers = set()
        contiguous_numbers.add(input_list[i])
        for j in range(i+1, len(input_list)):
            contiguous_numbers.add(input_list[j])
            total += input_list[j]
            if total == number:
                smallest_number = min(contiguous_numbers)
                largest_number = max(contiguous_numbers)
                return smallest_number + largest_number
            if total > number:
                break


number_to_sum_to = (find_invalid_number(input_numbers_list, 25, 25))
print(find_contiguous_numbers(number_to_sum_to, input_numbers_list))
