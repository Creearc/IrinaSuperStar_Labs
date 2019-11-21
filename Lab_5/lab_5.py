class Person(object):
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


class MyTime(object):
    def __init__(self, time):
        self.hour = int(time[0])
        self.minute = int(time[1])


class Room(object):
    def __init__(self, number, owner, time_in, time_out, visitor, document):
        self.number = number
        self.owner = Owner(owner, number)
        self.time_in = MyTime(time_in)
        self.time_out = MyTime(time_out)
        self.visitor = Visitor(visitor, document)

    def __repr__(self):
        return self.number


def is_late(room):
    for k in room:
        if k.time_in.hour > 20:
            yield k.number, "", ". Фамилия нарушителя: ", k.visitor
        else:
            yield k.number, "не", "", ""


def is_too_long(room):
    for k in room:
        if k.time_in.hour > k.time_out.hour or k.time_out.hour - k.time_in.hour >= 3:
            yield k.number, "долго", ". Фамилия нарушителя: ", k.visitor
        else:
            yield k.number, "приемлимое время", "", ""


if __name__ == "__main__":
    r = []
    r.append(Room(103, 'Назарова', (22, 5), (10, 8), 'Рассохин', 'Паспорт'))
    r.append(Room(603, 'Баринов', (20, 50), (23, 0), 'Боронников', 'Снилс'))
    r.append(Room(304, 'Балезина', (21, 10), (22, 15), 'Яковлева', 'Пропуск'))
    r.append(Room(404, 'Малышев', (19, 45), (22, 40), 'Морозов', 'Паспорт'))

    for n, l, e, v in is_late(r):
        print("Комнату %d посетили %s поздно%s%s." % (n, l, e, v))

    for n, l, e, v in is_too_long(r):
        print("Комнату %d посещали %s%s%s." % (n, l, e, v))
        
