""""Функция возведения числа в степень"""


def my_func(x, y):
	return x ** y


print(my_func(10, -3))


def my_func(x1, y1):
	i = 1
	x = 1
	while i <= abs(y1):
		result = x / x1
		x = result
		i += 1
	print(result)


my_func(10, -3)
