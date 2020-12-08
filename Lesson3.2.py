""""функция выводит введеную информацию."""


def function(name, sur, year, city, email, tel):

	print(f"Имя: {name}, Фамилия: {sur}, Год рождения: {year}, Город проживания: {city}, email: {email}, Телефон: {tel}")


function(input("Введите имя: "), input("Введите фамилию: "), input("Введите год рождения: "), input("Введите город проживания: "), input("Введите email: "), input("Введите телефон: "))
