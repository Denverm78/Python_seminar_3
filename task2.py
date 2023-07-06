# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# Строку в нижнем регистре в остальных случаях

data_user = input("Введите данные: ")

if data_user.isdecimal():
    print("Целое положительное число: ", data_user)
    
elif (data_user.count(".") == 1 and data_user.replace('.', '').isdigit()):
    print("Вещественное положительное число", data_user)

elif ((data_user.count(".") == 1) and (data_user[0] == '-') and (data_user.count("-") == 1) and \
      data_user.replace('.', '').replace('-', '').isdigit()): 
        print("Вещественное отрицательное число", data_user)
        
elif data_user.islower():
    print("Строка в нижнем регистре:", data_user.lower())

else:
    print("Строка в верхнем регистре:", data_user.upper())
          