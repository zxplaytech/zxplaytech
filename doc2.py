n = int(input("Введите номер места: "))
res = ""
if n % 2 == 0:
    res += "Верхнее "
else:
    res += "Нижнее "
if n > 36:
    res += "боковое"
else:
    res += "в купе"

print(res)
