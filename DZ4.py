n, m, k = map(int, input("Введите размеры шоколадки (n, m) и количество долек, которое необходимо отломить (k), через пробел: ").split())

if k > n*m:
    print("no")
elif k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")