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
        + visitors_doc(name, document)

class Room(pyDatalog.Mixin):
    def __init__(self, number, owner, time_in_h, time_in_m, time_out_h, time_out_m, visitor, document):
        super(Room, self).__init__()
        self.number = number
        self.owner = Owner(owner, number)
        + own(owner, number)
        self.time_in_h = time_in_h
        self.time_in_m = time_in_m
        self.time_out_h = time_out_h
        self.time_out_m = time_out_m
        self.visitor = Visitor(visitor, document)
        + visit(visitor, number)
        
    def __repr__(self): 
        return str(self.number)

def print_beautiful(data):
    for i in data:
        print(i[0])

if __name__ == "__main__":
    pyDatalog.create_terms('X, visit, own, visitors_doc')
    r = []
    r.append(Room(103, 'Назарова', 22, 5, 10, 8, 'Рассохин', 'Паспорт'))
    r.append(Room(603, 'Баринов', 20, 50, 23, 0, 'Боронников', 'Снилс'))
    r.append(Room(304, 'Балезина', 21, 10, 22, 15, 'Яковлева', 'Пропуск'))
    r.append(Room(404, 'Малышев', 19, 4, 22, 40, 'Морозов', 'Паспорт'))

    print('Кто из посетителей сдавал паспорт?')
    print_beautiful(visitors_doc(X, 'Паспорт'))
    
    print('________________________')
    print('Какую комнату посещал Рассохин?')
    print_beautiful(visit('Рассохин', X))

    print('________________________')
    print('Кто живет в комнате 404?')
    print_beautiful(own(X, 404))
    
    print('________________________')
    print('Посетители после 19 часов?')
    for i in Room.time_in_h[X] > 19:
        print("Номер комнаты %d" %(i[0].number))
        print_beautiful(visit(X, i[0].number))
