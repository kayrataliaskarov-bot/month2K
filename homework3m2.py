from datetime import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def age(self):
        day, month, year = map(int, self.__birth_date.split("."))
        birth = datetime(year, month, day)
        today = datetime.now()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def introduce(self):
        edu = "есть высшее образование" if self.__higher_education else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. У меня {edu}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия студент. Я учился в группе {self.group_name}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. "
              f"Моя профессия студент. Мое хобби {self.hobby}.")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()