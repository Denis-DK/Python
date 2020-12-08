from random import randint

with open("my_file_5.txt", mode="w+") as my_file:
	my_file.write(" ".join([str(randint(1, 1000)) for i in range(1000)]))
	my_file.seek(0)
	print(sum(map(int, my_file.readline().split())))
