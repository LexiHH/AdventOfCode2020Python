import re
from typing import Dict

with open("Day7Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')


def make_dictionary(input_string):
    bag_dictionary = {}
    for string in input_string:
        bag_colour = re.search(r".*?(?= bags contain)", string).group(0)
        inside_bags = re.findall(r"(?<=\d ).*?(?= bag)", string)
        inside_bag_numbers = re.findall(r"\d+", string)
        bag_dictionary[bag_colour] = {key: int(value) for key, value in zip(inside_bags, inside_bag_numbers)}
    return bag_dictionary


def sum_in_bag(bag_mapping: Dict, colour: str):
    number_children = 0
    child_bags = bag_mapping[colour]
    for child_colour, number_of_child_colour in child_bags.items():
        number_bags_in_child = sum_in_bag(bag_mapping, child_colour)
        number_children += number_of_child_colour + (number_of_child_colour * number_bags_in_child)
    print(colour, number_children)
    return number_children


global_bag_mapping = make_dictionary(input_list)
print(global_bag_mapping)
print(sum_in_bag(global_bag_mapping, "shiny gold"))
