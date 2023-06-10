from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record


class Name:
    def __init__(self, name):
        self.name = name


class Phone:
    def __init__(self, phone):
        self.value = phone


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone]



address_book = AddressBook()


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    address_book.add_record(rec)
    assert isinstance(address_book['Bill'], Record)
    assert isinstance(address_book['Bill'].name, Name)
    assert isinstance(address_book['Bill'].phones, list)
    assert isinstance(address_book['Bill'].phones[0], Phone)
    assert address_book['Bill'].phones[0].value == '1234567890'
    print('All Ok')