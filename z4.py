def div_x_by_3(number: int):
    return True if number % 3 == 0 else False


def div_100_by_x(number):
    res = None
    try:
        res = 100 / float(number)
    except ValueError:
        print("Ошибка: функция принимает только числа ")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print("Ошибка: ", e)
    return res


def magic_date_check(date: str):
    date = str(date)
    date = date.split(".")
    return True if int(date[0]) * int(date[1]) == int(date[2][2:]) else False


def lucky_number_check(ticket: str):
    sum1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    sum2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    return True if sum1 == sum2 else False


if __name__ == "__main__":
    print(div_x_by_3(7))
    print(div_x_by_3(9))
    print()
    print(div_100_by_x(5))
    print(div_100_by_x(0))
    print(div_100_by_x("number 5"))
    print()
    print(magic_date_check("22.01.2022"))
    print(magic_date_check("20.01.2022"))
    print()
    print(lucky_number_check("231002"))
    print(lucky_number_check("385916"))
