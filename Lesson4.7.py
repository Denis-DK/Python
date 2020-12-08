def func(num):
	f_num = 1
	if num == 0:
		yield f"{num}! = 1"
	for num in range(1, num + 1):
		f_num *= num
		yield f" {num}! = {f_num}"


for num in func(int(input("Факториал: "))):
	print(num)
