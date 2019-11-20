import pymorphy2

morth = pymorphy2.MorphAnalyzer()

text = """Морфологический анализ - это определение характеристик слова на
основе того, как это слово пишется. При морфологическом анализе не
используется информация о соседних словах."""

text = text.split()
for word in text:   
    s = morth.parse(word)
    print(s)
