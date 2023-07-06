# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

user_list = [1, 10, 5, 1, 5, 1, 7, 6, 7, 6, 6, 5, 10, 7, 10, 0, 8, 10, 10]
print("Исходный список: ", user_list)
result_list = []
for i in user_list:
    if user_list.count(i) > 1:
        if i not in result_list:
            result_list.append(i)
print("Результирующий список: ", result_list)
