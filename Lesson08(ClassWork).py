import os

print("-------------------------------------------- Работа с файлами")

# ---- Ш П А Р Г А Л К А ----
# r  — открывает файл только для чтения.
# w  — открывает файл только для записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для записи)
# w+ — открывает файл для чтения и записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для чтения и записи)
# a+ - открывает файл для чтения и записи.
#      (Информация добавляеться в конец файла)


# ВАРИАНТ 1 - Запись строчки "Example" в файл "kek.txt"
file = open("kek.txt", mode="w")
file.write("Example1")
file.close()
os.remove("kek.txt")  # Удаление Файла "kek.txt"

# ВАРИАНТ 2 - Запись строчки "Example" в файл "kek.txt" (использоване "with" автоматически закрывает файл)
with open("kek.txt", mode="w") as file:
    file.write("Example2")
os.remove("kek.txt")  # Удаление Файла "kek.txt"

# Чтение из файла "Lesson08(ClassWork).py"
with open("Lesson08(ClassWork).py", "r") as file:
    print(file.read(600))  # Читает первые 600 символов

print("-------------------------------------------- Обработка ошибок")

lst = [1, 2, 3]
x = 2
try:
    print(lst[x])
except IndexError:
    print('Список начинается с нулевого индекса, lst[{}] не существует!'.format(x))
finally:
    print('Что бы не произошло, этот текст отобразиться!')

