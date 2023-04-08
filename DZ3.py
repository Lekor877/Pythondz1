ticket_number = input("Введите номер билета: ")

if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Ошибка! Номер билета должен состоять из 6 цифр.")
else:
    sum_first_half = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    sum_second_half = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    if sum_first_half == sum_second_half:
        print("Yes")
    else:
        print("No")