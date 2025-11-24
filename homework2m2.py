class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.profession}")


class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник из группы {self.group_name}, "
              f"я родился {self.birth_date}, работаю {self.profession}")


class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг, мое хобби {self.hobby}, "
              f"я родился {self.birth_date}, работаю {self.profession}")


classmate1 = Classmate("Бектур", "5.12.2000", "программист", "Байэла")
classmate2 = Classmate("Айдана", "10.01.2001", "дизайнер", "Байэла")

friend1 = Friend("Алмаз", "15.08.1999", "инженер", "шахматы")
friend2 = Friend("Эмир", "20.03.2000", "маркетолог", "футбол")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()