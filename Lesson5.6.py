dic = {}
with open('my_file_6.txt', 'r', encoding="utf-8") as my_file:
	for line in my_file:
		timing = []
		lesson = ([el for el in line.split("")])
		for el in lesson:
			timing.append("".join(i for i in list(el) if i.isdigit()))
		result[line.split(':')[0]] = sum([int(i) for i in timing if i.isdigit()])
		result = sum([int(i) for i in timing if i.isdigit()])

print(result)
