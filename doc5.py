n = int(input("Введите количество слов: "))
res = []
for i in range(n):
    new_word = input()
    res.append(new_word)
res = " ".join(res)
print(res)
