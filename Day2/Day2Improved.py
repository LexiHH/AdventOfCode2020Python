from typing import Iterable
from Day2PasswordObject import PasswordObject

with open("Day2Input.txt") as file:
    read_data = file.read()

string_formatted = read_data.split('\n')


def make_password_objects(string_list_input):
    password_objects = []
    for string in string_list_input:
        password_object = PasswordObject.make_object_from_string(string)
        password_objects.append(password_object)
    return password_objects


def analyse_passwords_day_one(password_objects: Iterable[PasswordObject]):
    correct_passwords_count = 0
    for password_object in password_objects:
        if password_object.day_one_valid_password():
            correct_passwords_count += 1
    print(correct_passwords_count)


def analyse_passwords_day_two(password_objects: Iterable[PasswordObject]):
    correct_passwords_count = 0
    for password_object in password_objects:
        if password_object.day_two_valid_password():
            correct_passwords_count += 1
    print(correct_passwords_count)


password_objects = make_password_objects(string_formatted)
analyse_passwords_day_one(password_objects)
analyse_passwords_day_two(password_objects)





