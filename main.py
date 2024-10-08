# Запрашиваем 2 числа
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

# Наименьшее число
result = number1 if number1 < number2 else number2 if number1 > number2 else "Числа равны"

# Выводим
print(result)