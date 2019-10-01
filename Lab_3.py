class Person(object):
    def __init__(self, name):
        self.name = name

class Owner(Person):
    def __init__(self, name, room_number):
        Person.__init__(self, name)
        self.room_number = room_number

class Visitor(Person):
    def __init__(self, name, document):
        Person.__init__(self, name)
        self.document = document

class MyTime(object):
    def __init__(self, time):
        self.hour = int(time[0])
        self.minute = int(time[1])

class Room(object):
    def __init__(self, number, owner, time, visitor, document):
        self.number = number
        self.owner = Owner(owner, number)
        self.time = MyTime(time)
        self.visitor = Visitor(visitor, document)
