book = []  # Объявление переменной соответствует требованиям PEP8

# Для соблюдения требований PEP8 строка была разбита на несколько строк
# Перенос строки соответствует требованиям PEP8
# Пробелы после двоеточий и запятых, а также их отсутствие перед этими знаками
# соответствуют требованиям PEP8
book.append({"Room_number": 105, "Surname": 'Назарова',
             "Arrival_time": (22, 5), "Departure_time": (8, 10),
             "Guest_info": 'Рассохин', "Document": 'Трудовая книжка'})

book.append({"Room_number": 603, "Surname": 'Баринов',
             "Arrival_time": (20, 50), "Departure_time": (23, 0),
             "Guest_info": 'Мартонова', "Document": 'пропуск'})
book.append({"Room_number": 304, "Surname": 'Яковлева',
             "Arrival_time": (21, 10), "Departure_time": (22, 15),
             "Guest_info": 'Балезина', "Document": 'Водительские права'})
book.append({"Room_number": 407, "Surname": 'Боронников',
             "Arrival_time": (19, 45), "Departure_time": (22, 40),
             "Guest_info": 'Малышев', "Document": 'снилс'})
book.append({"Room_number": 404, "Surname": 'Найденов',
             "Arrival_time": (21, 30), "Departure_time": (23, 0),
             "Guest_info": 'Морозов', "Document": 'паспорт'})
print(book)

