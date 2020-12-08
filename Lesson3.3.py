""""Функия выводит сумму двух наибольших, введеных, чисел."""


def choice(arg1, arg2, arg3):

	if arg1 >= arg2 >= arg3:
		print(arg1 + arg2)
	elif arg2 < arg1 < arg3:
		print(arg1 + arg3)
	else:
		print(arg2 + arg3)


choice(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))
