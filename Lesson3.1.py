""""" Функция деления."""


def division(arg_one=int(input("Введите первое число ")), arg_two=int(input("Введите второе число "))):
	while arg_two == 0:
		arg_two = int(input('Введите число не равное "0" '))

	result = arg_one / arg_two
	print(f"Результат деления: {result}")


division()
