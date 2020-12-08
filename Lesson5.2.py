my_file = open("my_file_2.txt", "r")
content = my_file.read()
print(f"Текст файла:\n {content}")

my_file = open("my_file_2.txt", "r")
content = my_file.readlines()
print(f"Кол-во строк: {len(content)}")

my_file = open("my_file_2.txt", "r")
content = my_file.readlines()
for i in range(len(content)):
	print(f"Кол-во символов {i + 1} строки: {len(content[i])}")

my_file = open("my_file_2.txt", "r")
content = my_file.read()
content = content.split()
print(f"Кол-во слов: {len(content)}")
my_file.close()
