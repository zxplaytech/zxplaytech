import random

wrong_counter = 0
right_counter = 0
while wrong_counter < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"{a} + {b} = ", end="")
    res = int(input())
    if a+b == res:
        right_counter += 1
        print("Правильно!")
    else:
        wrong_counter += 1
        print("Ответ неверный.")


print("Игра окончена. Правильных ответов: ", right_counter, end="")
