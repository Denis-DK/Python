dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("my_file_4.1.txt", "w", encoding='utf-8') as my_file_new:
	with open("my_file_4.txt", encoding='utf-8') as my_file:
		my_file_new.writelines([line.replace(line.split()[0], dic.get(line.split()[0])) for line in my_file])
	