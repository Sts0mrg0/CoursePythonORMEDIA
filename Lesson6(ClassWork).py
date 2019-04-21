print("-------------------------------------------- Создание класса. Создание экзепляра. Процедура инициализации.")


# Класс  — это тип, описывающий устройство объектов.
# Объект — это экземпляр класса. Объект-представитель определенного класса.
# Атрибусы класса - переменные и данные класса
# Методы класса - функции класса

# ИНКАПСУЛЯЦИЯ
#   Способность сокрытии внутренних данных класса, для упрощения работы и предотвращения поломки (вмешательства извне)
#   Принцип: Используем класс без прямого доступа в его структуру.
# АБСТРАКЦИЯ
#   Способность моделирования упрощенного класса для решения конкретной проблемы.
#   Все объект и не обязательно чтобы он имел атрибуты и методы из реальной жизни.
# ПОЛИМОРФИЗМ
#   Способность создания методов (интерфейсов) которые могут обрабатывать разные типы данных (разные базовые формы).
#   Пример: print("тип строка") print(666)
# НАСЛЕДОВАНИЕ
#   Способность класса наследовать методы и атрибуты от другого класса.
#   Родительский класс - класс от которого наследуем. Дочерний класс - класс который наследует.
#   Множественное наследование - это наследование от нескольких родительских классов.
#   Дочерний класс не затрагивает родительский.

class Movie:
    valueMax = 100
    valueMin = 5

    # Выполнится при создании экземпляра
    def __init__(self):
        print("Экземпляр класса создан")


# Создание экземпляра класса "Movie()" под именем "x"
x = Movie()

# Вывод данных без создния экзепляра
print(Movie.valueMin, Movie.valueMax)

# Вывод данных экземпляра "x"
print(x.valueMin, x.valueMax)

print("-------------------------------------------- Класс Orange(Апельсин). Создание экхемпляров. Метод очистки.")


class Orange:
    def __init__(self, color, size, view):
        self.color = color
        self.size = size
        self.view = view
        print("Аппельсин создан")
        print("Его параметры:", "ЦВЕТ:", self.color, "РАЗМЕР:", self.size, "ВНЕШНИЙ ВИД:", self.view)

    # Метод "Очистить кожуру"
    def peelOff(self):
        self.view = "Очищен от кожуры"
        print("Параметры:", "ЦВЕТ:", self.color, "РАЗМЕР:", self.size, "ВНЕШНИЙ ВИД:", self.view)


# Создаем наши апельсины
oneOrange = Orange("черный", "большой", "без дефектов")
twoOrange = Orange("оранжевый", "средний", "помятый")
threeOrange = Orange("красный", "маленький", "без дефектов")

# Чистим наши апельсины
oneOrange.peelOff()
twoOrange.peelOff()
threeOrange.peelOff()

print("-------------------------------------------- Пример НАСЛЕДОВАНИЯ и ПЕРЕОПРЕДЕЛНИЯ МЕТОДА")


class OneClass():  # Родительский
    x = 10
    y = 20

    def __init__(self):
        print("Объект создан")


class TwoClass(OneClass):  # Дочерний (Наследует все атрибуты и методы)
    def __init__(self, a, b):  # Переопределение метода или атрибуда в дочернем классе (просто пишем такое же название)
        self.a = a
        self.b = b
        print("Объект создан")


One = OneClass()
Two = TwoClass(30, 40)

print(One.x, One.y)
print(Two.x, Two.y, Two.a, Two.b)  # В объекте "Two" есть переменные(атрибуты) "x" и "y" унаследованные от "One"

print("-------------------------------------------- ПАРСИНГ")

# Парсинг      — это инструмент работы со строковыми данными. 
# Веб Скрапинг – это процесс извлечения информации из сайта.
# Краулинг     - это переход программы от одной ссылки к другой чтобы собрать всю информацию.

import requests

from bs4 import BeautifulSoup as bs


def get_html(url):
    res = requests.get(url)             # Возвращает <Response [200]> статус результа запроса
    res_dir = dir(requests.get(url))    # Dir – возвращает список всех атрибутов.
    res_text = requests.get(url).text   # Возвращает HTML ответ
    print("-------------1-------------", res)
    print("-------------2-------------", res_dir)
    #print("-------------3-------------", res_text)



print(get_html("https://ru.wordpress.org/"))

