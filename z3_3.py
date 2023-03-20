while (new_word := str(input())) != "stop":
    if "ф" in new_word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")


