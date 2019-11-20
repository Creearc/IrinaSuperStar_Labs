def foo():

    yield 'Супер'

    yield 'Пупер'

    yield 'Дупер'

    yield 'Стар'

for i in foo():
    print(i)
