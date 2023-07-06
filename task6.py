# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

user_string = input("Введите строку: ")
split_list = user_string.split(' ')
# print(split_list)
split_list.sort()
max_len = 0
for i in split_list:
    if len(i) > max_len:
        max_len = len(i)
for i, item in enumerate(split_list):
    print((i + 1), item.rjust(max_len, ' '))
