from pyDatalog import pyDatalog 

class Person(pyDatalog.Mixin):
    def __init__(self, name):
        self.name = name 
    def __repr__(self): 
        return self.name

class Owner(Person):
    def __init__(self, name, room_number):
        Person.__init__(self, name)
        self.room_number = room_number

class Visitor(Person):
    def __init__(self, name, document):
        Person.__init__(self, name)
        self.document = document

class MyTime(pyDatalog.Mixin):
    def __init__(self, time):
        self.hour = int(time[0])
        self.minute = int(time[1])
    def __repr__(self): 
        return str(self.hour), str(self.minute)

class Room(pyDatalog.Mixin):
    def __init__(self, number, owner, time_in, time_out, visitor, document):
        super(Room, self).__init__()
        self.number = number
        self.owner = Owner(owner, number)
        self.time_in = MyTime(time_in)
        self.time_out = MyTime(time_out)
        self.visitor = Visitor(visitor, document)
    def __repr__(self): 
        return str(self.number)

if __name__ == "__main__":
    r = []
    r.append(Room(103, 'Назарова', (22, 5), (10, 8), 'Рассохин', 'Паспорт'))
    r.append(Room(603, 'Баринов', (20, 50), (23, 0), 'Боронников', 'Снилс'))
    r.append(Room(304, 'Балезина', (21, 10), (22, 15), 'Яковлева', 'Пропуск'))
    r.append(Room(404, 'Малышев', (19, 45), (22, 40), 'Морозов', 'Паспорт'))

    pyDatalog.create_terms('X')
    print(Room.number[X] > 300)
