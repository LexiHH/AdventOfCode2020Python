import re


class PasswordObject:
    def __init__(self, min_number, max_number, letter, password):
        self.min_number = int(min_number)
        self.max_number = int(max_number)
        self.letter = letter
        self.password = password

    def calc_number_of_matches(self):
        return len(re.findall(self.letter, self.password))

    def day_one_valid_password(self):
        return self.min_number <= self.calc_number_of_matches() <= self.max_number

    def day_two_valid_password(self):
        letter_at_min_number = self.password[self.min_number-1]
        letter_at_max_number = self.password[self.max_number-1]
        return (letter_at_min_number == self.letter and letter_at_max_number != self.letter) or \
               (letter_at_max_number == self.letter and letter_at_min_number != self.letter)

    @classmethod
    def make_object_from_string(cls, string):
        min_number = re.search(".*?(?=-)", string).group(0)
        max_number = re.search("(?<=-)(.*?)(?=\ )", string).group(0)
        letter = re.search("(?<=\ )(.*?)(?=:)", string).group(0)
        password = re.search("(?<=:\ )(.*)", string).group(0)
        return cls(min_number, max_number, letter, password)
