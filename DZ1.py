number = input("Введите трехзначное число: ")

# Проверяем, что введено трехзначное число
if len(number) != 3 or not number.isdigit():
    print("Ошибка! Нужно ввести трехзначное число.")
else:
    # Считаем сумму цифр
    sum_of_digits = int(number[0]) + int(number[1]) + int(number[2])
    print(f"Сумма цифр числа {number} равна {sum_of_digits}.")