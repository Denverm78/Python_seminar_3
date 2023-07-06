# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friend_dict = {"Иван": ("нож", "лопата", "котелок", "спальник", "фотоаппарат", "палатка", "топор", "веревка", "вилка"), \
               "Сергей": ("палатка","спальник","фонарик","нож","спички","мангал", "вилка"), \
                "Виктор":("спальник", "палатка", "гитара", "спички", "веревка")}
""" name_new_friend = input("Добавьте имя друга: ")
things_new_friend = tuple(input("Введите список вещей друга через пробел: ").split(" "))
friend_dict[name_new_friend] = things_new_friend
print(friend_dict) """
set_1 = set(friend_dict["Иван"])
set_2 = set(friend_dict["Сергей"])
set_3 = set(friend_dict["Виктор"])
set_123 = set_1 | set_2 | set_3 # Список всех вещей
print("Список всех вещей", set_123) 
set_same_123 = set_1 & set_2 & set_3
print("Список одинаковых вещей", set_same_123)
set_unic_1 = set_123 - set_2 - set_3
print("Уникальные вещи у Ивана: ", set_unic_1)
set_unic_2 = set_123 - set_1 - set_3
print("Уникальные вещи у Сергея: ", set_unic_2)
set_unic_3 = set_123 - set_1 - set_2
print("Уникальные вещи у Виктора: ", set_unic_3)
set_not_1 = set_2 & set_3 - set_1
print("Только у Ивана нет", set_not_1)
set_not_2 = set_1 & set_3 - set_2
print("Только у Сергея нет", set_not_2)
set_not_3 = set_1 & set_2 - set_3
print("Только у Виктора нет", set_not_3)