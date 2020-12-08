import re

with open("Day8Input.txt") as file:
    read_data = file.read()

input_list = read_data.split('\n')


def make_dictionary(input_string):
    instruction_dictionary = {}
    count = 0
    for string in input_string:
        count += 1
        instruction = re.search(".*?(?= )", string).group(0)
        number = int(re.search("(?<= ).*", string).group(0))
        instruction_dictionary[count] = (instruction, number)
    return instruction_dictionary


def execute_instructions(instructions):
    instruction = 1
    instruction_set = set()
    count_instructions = 0
    accelerate = 0
    while instruction <= len(instructions):
        instruction_type, calculation_amount = instructions.get(instruction)
        if instruction in instruction_set:
            return True, accelerate, count_instructions
        else:
            count_instructions += 1
            instruction_set.add(instruction)
            if instruction_type == 'nop':
                instruction += 1
            elif instruction_type == 'acc':
                accelerate += calculation_amount
                instruction += 1
            elif instruction_type == 'jmp':
                instruction += calculation_amount
    return False, accelerate


def break_infinite_loop(original_dictionary):
    for dictionary_item in original_dictionary.items():
        new_dictionary = dict(original_dictionary)
        instruction_number = dictionary_item[0]
        instruction_type = dictionary_item[1][0]
        calculation_amount = dictionary_item[1][1]
        if instruction_type == 'nop':
            new_dictionary[instruction_number] = ('jmp', calculation_amount)
        elif instruction_type == 'jmp':
            new_dictionary[instruction_number] = ('nop', calculation_amount)
        results = (execute_instructions(new_dictionary))
        if not results[0]:
            return results[1]


dictionary = make_dictionary(input_list)
print(break_infinite_loop(dictionary))
