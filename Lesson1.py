name = input("Введите Ваше имя: ")
age = input("Введите свой возвраст : ")
print(f"Привет {name} тебе {age}")

time = int(input("За сколько секунд ты пробежишь марафон? "))
hours = time // 3600
minute = (time - hours * 3600) // 60
seconds = (time - (hours * 3600 + minute * 60))
print(f"{hours}:{minute}:{seconds}")

number = (input("Введи любое число "))
num = [int(number), int(number+number), int(number+number+number)]
sum_num = num[0] + num[1] + num[2]
print(f"Сумма типа n+nn+nnn твоего числа равна: {sum_num}")

n = abs(int(input("Ведите целое положительное число ")))
m = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > m:
        m = n % 10
    if n > 9:
        continue
    else:
        print(f"В Вашем числе максимальная цифра: {m}")
        break

proceeds = int(input("Введите выручку: "))
costs = int(input("Введите затраты: "))
if proceeds > costs:
    profitability = (proceeds-costs) / proceeds
    print(f"Рентабельность составила: {profitability:.2f}")
    emloyes = int(input("Сколько у вас в фирме работников? "))
    print(f"Прибыль на 1 FTE составила: {(proceeds-costs)/emloyes:.2f}")
else:
    print(f"У вас убытки в размере: {proceeds-costs}")


now = int(input("Сколько ты пробегаешь сейчас? "))
target = int(input("Сколько ты хочешь пробегать? "))
day = 1
result = now
while now < target:
    now = now + (now * 0.1)
    day += 1
    result = now + result
print(f"Улучшая свой результ каждый день на  10%, ты достигнешь цели {target} км на {day} день")

my_list = [2, 5, 9]
user = int(input("num "))

if user in my_list:
    i = my_list.index(user)
    my_list.insert(i, user)
    print(my_list)
else:
    my_list.append(user)
    print(my_list)
