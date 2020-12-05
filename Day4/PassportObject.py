import re


class PassportObject:
    def __init__(self, birth_year, issue_year, expiration_year, height, hair_colour, eye_colour, passport_id, country_id):
        self.birth_year = birth_year
        self.issue_year = issue_year
        self.expiration_year = expiration_year
        self.height = height
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        self.passport_id = passport_id
        self.country_id = country_id

    def all_attributes_but_cid(self):
        for attr, value in self.__dict__.items():
            if value is False:
                return False
        return True

    @staticmethod
    def check_digits(string, min, max):
        if string.isdigit():
            if min <= int(string) <= max:
                return True
        return False

    @staticmethod
    def height_checker(string):
        if 'in' in string:
            numbers = int(re.search("[0-9]+", string).group(0))
            if 50 <= numbers <= 76:
                return True
        elif 'cm' in string:
            numbers = int(re.search("[0-9]+", string).group(0))
            if 150 <= numbers <= 193:
                return True
        return False

    @staticmethod
    def hair_checker(string):
        if string[0:1] == '#' and len(string) == 7:
            if string[1:].isalnum():
                return True
        return False

    @staticmethod
    def eye_checker(string):
        allowed_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if len(string) == 3 and string in allowed_colours:
            return True
        return False

    @staticmethod
    def passport_checker(string):
        if string.isdigit() and len(string) == 9:
            return True
        return False


    @classmethod
    def make_object_from_string(cls, string):
        birth_year, issue_year, expiration_year, height, hair_colour, eye_colour, passport_id, country_id = \
            False, False, False, False, False, False, False, True
        if 'byr' in string:
            birth_year_result = re.search("(?<=byr:)(\S*)", string).group(0)
            birth_year = PassportObject.check_digits(birth_year_result, 1920, 2002)
        if 'iyr' in string:
            issue_result = re.search("(?<=iyr:)(\S*)", string).group(0)
            issue_year = PassportObject.check_digits(issue_result, 2010, 2020)
        if 'eyr' in string:
            expiration_result = re.search("(?<=eyr:)(\S*)", string).group(0)
            expiration_year = PassportObject.check_digits(expiration_result, 2020, 2030)
        if 'hgt' in string:
            height_result = re.search("(?<=hgt:)(\S*)", string).group(0)
            height = PassportObject.height_checker(height_result)
        if 'hcl' in string:
            hair_result = re.search("(?<=hcl:)(\S*)", string).group(0)
            hair_colour = PassportObject.hair_checker(hair_result)
        if 'ecl' in string:
            eye_result = re.search("(?<=ecl:)(\S*)", string).group(0)
            eye_colour = PassportObject.eye_checker(eye_result)
        if 'pid' in string:
            passport_id_result = re.search("(?<=pid:)(\S*)", string).group(0)
            passport_id = PassportObject.passport_checker(passport_id_result)
        return cls(birth_year, issue_year, expiration_year, height, hair_colour, eye_colour, passport_id, country_id)


