from itertools import count, cycle

print('Для выхода введите - "q" или при достижении числа = 10 цикл заверешится')
for num in count(int(input("Введите число: "))):
	print(num, end='')
	stop = input()
	if stop == 'q':
		break
	if num == 10:
		break

print("Повторяет элементы списка. Для повторения Enter, для выхода - q")
my_list = input("Введите через пробел список: ").split()
item = cycle(my_list)
stop = None

while stop != 'q':
	print(next(item), end='')
	stop = input()
