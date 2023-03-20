res = []
while new_word := input():
    if new_word =="stop":
        break
    else:
        res.append(new_word)

res = " ".join(res)
print(res)