# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

def backpack(capacity: int, thing_list: dict):
    result_list = []
    summ = 0   
    for key, value in thing_list.items():
        if value <= capacity:            
            result_list.append(key)
            capacity = capacity - value           
            summ = summ + value
    return result_list, summ

# Вес предметов условный, так как не получалось работать с вещественными числами из-за неточности - последний предмет не влезал в рюкзак

user_list = {"нож":2, "лопата":15, "котелок":17, "спальник":38, "фотоаппарат":11, "палатка":45, \
    "топор":40, "веревка":6, "вилка":2, "кружка":4, "ложка":2, "горючее":1}
capacity = int(input("Укажите вместимость рюкзака: "))
print()

sorted_list_1 = {} # Сортируем от самого тяжелого к самому легкому
sorted_keys = sorted(user_list, key=user_list.get, reverse=True)  
for i in sorted_keys:
    sorted_list_1[i] = user_list[i]
    
sorted_list_2 = {} # Сортируем от самого легкого к самому тяжелому
sorted_keys = sorted(user_list, key=user_list.get, reverse=False)  
for i in sorted_keys:
    sorted_list_2[i] = user_list[i]    

full_backpack_1 = (backpack(capacity, sorted_list_1))
print("Вариант 1:")
print(f"В рюкзак вместятся: {full_backpack_1[0]}")
print(f"Вес рюкзака составит: {full_backpack_1[1]}")
print()

full_backpack_2 = (backpack(capacity, sorted_list_2))
print("Вариант 2:")
print(f"В рюкзак вместятся: {full_backpack_2[0]}")
print(f"Вес рюкзака составит: {full_backpack_2[1]}")
print()
      