# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data_user = (5, 3.141, 'Привет', 5==5, 7, 67.34, 'Hello', 100, False)
result_tuple = {}
elements_list = []
for i in data_user:
    if type(i) not in result_tuple.keys():
        elements_list.append(i)
        # print(elements_list)
        result_tuple[type(i)] = elements_list
    else:
        result_tuple[type(i)].append(i)
    elements_list = []                
print(result_tuple)
    