class Student(object):
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

    @classmethod
    def from_string(cls, name_str):
        is_full_name = Student.is_full_name(name_str)
        first_name, last_name = name_str.split(' ')
        student = cls(first_name, last_name)
        return student


a = [1, 2, 3, 4]
b, c, *rest = a
print(rest)

scott = Student.from_string('Scott Robinson')
print(scott)
