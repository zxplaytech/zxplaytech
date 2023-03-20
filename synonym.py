while True:
    word = str(input("Введите слово: ")).lower()
    if word == "exit": break
    words = dict()
    with open("synonyms.txt","r") as file:
        for line in file:
            if line.split("-")[0].strip() in words.keys():
                words[line.split("-")[0].strip()] = words[line.split("-")[0].strip()] + " " + line.split("-")[1].strip()
            else:
                words[line.split("-")[0].strip()] = line.split("-")[1].strip()
    if word in words.keys():
        print("Найдены синонимы: ")
        print(words[word])
    else:
        print("Синонимы не найдены")
    print("Добавить новый синоним для этого слова? y/n", end=" ")
    answer = str(input())
    if answer.strip() == "y":
        print("Введите новый синоним")
        new_word = str(input())
        if word in words:
            if words[word].endswith(";"):
                words[word] = words[word] + " " + new_word
            else:
                words[word] = words[word] + "; " + new_word
        else:
            words[word] = new_word
        with open("synonyms.txt","w") as file:
            for i in words:
                file.write(str(i) + " - " + str(words[i]) + "\n")
        print("Синоним добавлен")

