class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number

    @staticmethod
    def validate_phone_number(phone_number):

        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр!")

        new_contact = Contact(name, phone_number)


        cls.all_contacts.append(new_contact)



print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0950213456")

for c in ContactList.all_contacts:
    print(c.name, c.phone)