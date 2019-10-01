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


def test(data, space):
    for s in data.__dir__():
        if s == "__class__": break
        attr = data.__getattribute__(s).__repr__()
        if attr[1:10] == "built-in" or attr[1:10] == "method-wr": break
        print("%s%s" % (space, attr))
        test(data.__getattribute__(s), space + "  ")


if __name__ == "__main__":
    # t = MyTime((10, 9))
    # print(t.hour)
    r = Room(103, 'Назарова', (10, 8), 'Рассохин', 'Паспорт')
    # print(r.number, r.time.hour, r.owner.name, r.visitor.document)
    test(r, "")

