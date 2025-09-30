class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email
    def show(self):
        print(self.name + ' - ' + self.email)

class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    def show(self):
        Person.show(self)
        Address.show(self)
        

class Notebook:
    def __init__(self, contacts=None):
        if contacts is not None:
            self.contacts = contacts
        else:
            self.contacts = {}
    
    def show(self):
        for name, contact in self.contacts.items():
            print(f"=== {name} ===")
            contact.show()
            print("-----")

    def add(self, name, email, street, city):
        self.contacts[name] = Contact(street, city, name, email)


notes = Notebook()
notes.add('Alice', '<alice@example.com>', 'Lv 24', 'Sthlm')
notes.show()