# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

user_list = [1, 10, 5, 1, 5, 1, 7, 6, 7, 6, 6, 5, 10, 7, 10, 0, 8, 10, 10]
for i in user_list:
    if user_list.count(i) > 1:
        user_list.remove(i)
for i in user_list:
    if user_list.count(i) > 1:
        user_list.remove(i)    
print(user_list)
