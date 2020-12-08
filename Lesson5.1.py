my_file = open("my_file.txt", "w")

while True:
	text = my_file.write(input("Введите текст: "))
	if not text:
		break

my_file.close()

my_file = open("my_file.txt", "r")
content = my_file.readline()
print(content)
my_file.close()
