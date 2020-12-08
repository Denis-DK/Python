# --- 1 ---
list_style = ["Стол", 85, 22.3, "Стул", True]
for x in list_style:
	print(type(x))

# --- 2 ---
user_list = input("Введите значения списка: ").split()
i = 0
while i + 1 < len(user_list):
	if i % 2 == 0:
		user_list.insert(i, user_list.pop(i + 1))
	i += 1
print(user_list)

# --- 3 ---
sesson = ['Зима', 'Весна', 'Лето', 'Осень']
mounth = int(input("Введите месяц в виде целого числа: "))

if mounth == 1 or mounth == 2 or mounth == 12:
	print(sesson[0])
elif mounth == 3 or mounth == 4 or mounth == 5:
	print(sesson[1])
elif mounth == 6 or mounth == 7 or mounth == 8:
	print(sesson[2])
elif mounth == 9 or mounth == 10 or mounth == 12:
	print(sesson[3])
else:
	print('Вы ввели не коректное значение')

# --- 4 ---
text = input("Введите прдложение: ")
user_text = text.split()
w = 0
for x in user_text:
	if len(x) > 10:
		print(f"{w + 1}. {x[0:10]}")
		w += 1
	else:
		print(f"{w + 1}. {x}")
		w += 1

# --- 5 ---
my_list = [7, 8, 5, 6, 3, 9, 1]
user_num = int(input("Введите число: "))

if user_num in my_list:
	i = my_list.index(user_num)
	my_list.insert(i + 1, user_num)
	print(my_list)

else:
	my_list.append(user_num)
	print(my_list)
