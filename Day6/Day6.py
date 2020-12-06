from collections import Counter

with open("Day6Input.txt") as file:
    read_data = file.read()


def format_questionnaires(input_string):
    input_list_with_blanks = input_string.split('\n\n')
    input_list = [x for x in input_list_with_blanks if x]
    list_of_groups = []
    for group in input_list:
        list_of_groups.append(group.split('\n'))
    return list_of_groups


def sum_questionnaires_anyone(groups):
    sum = 0
    for group in groups:
        group_unique_questions = set()
        for person in group:
            for question in person:
                group_unique_questions.add(question)
        sum += len(group_unique_questions)
    print(sum)


def sum_questionnaires_everyone(groups):
    sum = 0
    for group in groups:
        number_of_people = len(group)
        question_count = Counter()
        for person in group:
            for question in person:
                question_count.update(question)
        for value in question_count.values():
            if value == number_of_people:
                sum += 1
    return sum




questionnaires = format_questionnaires(read_data)
print(sum_questionnaires_everyone(questionnaires))