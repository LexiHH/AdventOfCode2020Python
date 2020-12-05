from PassportObject import PassportObject

with open("Day4Input.txt") as file:
    read_data = file.read()


def format_passports(input_string):
    input_list_with_blanks = input_string.split('\n\n')
    input_list = [x for x in input_list_with_blanks if x]
    passports = []
    for passport in input_list:
        passport = passport.replace('\n', ' ')
        passports.append(PassportObject.make_object_from_string(passport))
    return passports


def number_valid_passports(passports):
    count = 0
    for passport in passports:
        if passport.all_attributes_but_cid():
            count += 1
    print(count)


passports = format_passports(read_data)
number_valid_passports(passports)



