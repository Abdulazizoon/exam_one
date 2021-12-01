def depozit(num):
    res = (0.12 / 12 * num + num)
    print(f"Первый месяц -> {res}")
    res2 = (0.12 / 12 * res + res)
    print(f"Второй месяц -> {res2}")
    res3 = (0.12 / 12 * res2 + res2)
    print(f"Третий месяц -> {res3}")
    res4 = (0.12 / 12 * res3 + res3)
    print(f"Четвертый месяц -> {res4}")
    res5 = (0.12 / 12 * res4 + res4)
    print(f"Пятый месяц -> {res5}")
    res6 = (0.12 / 12 * res5 + res5)
    print(f"Шестой месяц -> {res6}")

num1 = int(input("Введите сумму депозита: "))
depozit(num1)


