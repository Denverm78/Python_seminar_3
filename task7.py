# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

# Используем count

user_string = input("Введите строку: ")

# Используем count

user_dict_1 = {}
for i in user_string:
    if i in user_dict_1.keys():
        continue
    else:
        user_dict_1[i] = user_string.count(i)
print(user_dict_1)

# Более быстрый способ

user_dict_2 = {}
user_set = set(user_string)
for i in user_set:
    if i in user_dict_2.keys():
        continue
    else:
        user_dict_2[i] = user_string.count(i)
print(user_dict_2)
