with open("Day3Input.txt") as file:
    read_data = file.read()

string_formatted = read_data.split('\n')


def count_trees(string_list):
    i = 0
    tree = '#'
    count = 0
    for string in string_list:
        string_length = len(string)
        letter = string[(i % string_length)]
        i += 3
        if tree in letter:
            count += 1
    return count


print(count_trees(string_formatted))
