# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков. 

my_list = [3, 8, 25, 91, 4, 8, 91, 100, 3, 1, 5, 12]
print("Исходный список", my_list)
#list1 = set(my_list)
#print(list1)
#list2 = list(list1)
#print(list2)
result_list1 = list(set(my_list))
print("Уникальный список 1",result_list1)

# Способ 2
result_list2 = []
for i in my_list:
    if i not in result_list2:
        result_list2.append(i)
print("Уникальный список 2", result_list2)

