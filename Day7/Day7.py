import re

with open("Day7Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')
matching_bags_list_global = []
count = 0


def make_dictionary(input_string):
    bag_dictionary = {}
    for string in input_string:
        bag_colour = re.search(r".*?(?= bags contain)", string).group(0)
        inside_bags = re.findall(r"(?<=\d ).*?(?= bag)", string)
        inside_bag_numbers = re.findall(r"\d+", string)
        bag_dictionary[bag_colour] = {key: value for key, value in zip(inside_bags, inside_bag_numbers)}
    print(bag_dictionary)
    return bag_dictionary


def get_bags(bag_colour_required, matching_bags_list, dictionary):
    for outer_bag, inner_bags in dictionary.items():
        for bag_colour, bag_number in inner_bags.items():
            if bag_colour == bag_colour_required:
                matching_bags_list.append(outer_bag)
    return matching_bags_list


def get_bags_loop(matching_bags_list, dictionary):
    orig_list_length = 0
    new_list_length = 1
    while new_list_length > orig_list_length:
        for bag_colour in matching_bags_list:
            orig_list_length = len(matching_bags_list)
            matching_bags_list = get_bags(bag_colour, matching_bags_list, dictionary)
    return matching_bags_list


def count_bags(bags_list):
    bags_set = set(bags_list)
    return len(bags_set)


bag_dictionary_global = make_dictionary(input_list)
print(
    count_bags(
        get_bags_loop(
            get_bags("shiny gold", matching_bags_list_global, bag_dictionary_global),
            bag_dictionary_global
        )
    )
)
