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
    while instruction < len(instructions):
        instruction_type, instruction_number = instructions.get(instruction)
        if instruction in instruction_set:
            return accelerate, count_instructions
        else:
            count_instructions += 1
            instruction_set.add(instruction)
            if instruction_type == 'nop':
                instruction += 1
            elif instruction_type == 'acc':
                accelerate += instruction_number
                instruction += 1
            elif instruction_type == 'jmp':
                instruction += instruction_number


dictionary = make_dictionary(input_list)
print(execute_instructions(dictionary))
