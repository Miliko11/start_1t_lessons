sum = 0
for iteration in range(1, 10+1): # 10+1 чтобы учитывалось 10. можно и просто 11 написать
    x = int(input("Введите номинал монеты: "))
    if x <= 0 or x == 3 or x == 4 or 6 <= x < 10:
        continue
    sum = sum + x
    print("Сумма= ", sum)
    if sum >= 100:
        break
else:
    print("Вы сбросили 10 монет, суммирование в цикле завершено!")
print('Итого накопили:', sum)

