# ----1----
from time import sleep


class TrafficLight:
	__color = ["Красный", "Желтый", "Зеленый"]

	def running(self):
		i = 0
		while i < 3:
			print(f'Цвет сфетофора {TrafficLight.__color[i]}')
			if i == 0:
				sleep(7)
			elif i == 1:
				sleep(2)
			elif i == 2:
				sleep(7)
			i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


# ----2----
class Road:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def mass(self):
		return self.length * self.width


r = Road(20, 5000)
print(f"Масса асфальта: {r.mass() * 25 * 5 / 1000} т.")


# ----3----
class Worker:

	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

	def __init__(self, name, surname, position, wage, bonus):
		Worker.__init__(self, name, surname, position, wage, bonus)

	def get_full_name(self):
		return self.name + " " + self.surname

	def get_total_income(self):
		return self.income.get("wage") + self.income.get("bonus")


full_name = Position("John", "Doe", "Worker", 2000, 500)
print(f"Полное имя работника: {full_name.get_full_name()}")
print(f"Должнлсть работника: {full_name.position}")
print(f"Доход с учетом премии: {full_name.get_total_income()}")


# ----4----
class Car:

	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		return f'{self.name} поехала'

	def stop(self):
		return f'{self.name} остановилась'

	def turn_left(self):
		return f'{self.name} повернула налево'

	def turn_right(self):
		return f'{self.name} повернула направо'

	def show_speed(self):
		return f'Скорость {self.name}: {self.speed}'


class TownCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		print(f" {self.name} {self.speed}")
		if self.speed > 60:
			return f'Скорость {self.name} привышена'
		else:
			return f'Скорость {self.name} без превышения'


class SportCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


class WorkCar(Car):

	def __init__(self, spped, color, name, is_police):
		super().__init__(spped, color, name, is_police)

	def show_speed(self):
		print(f'{self.name} {self.speed}')
		if self.speed > 40:
			return f'Скорость {self.name} превышена'
		else:
			return f'Скорость {self.name} без превышения'


class PoliceCar(Car):

	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

	def police(self):
		if self.is_police:
			return f"{self.name} принадлежит МВД"
		else:
			return f"{self.name} не принадлежит МВД"


audi = TownCar(80, 'Red', 'Audi', False)
ford = PoliceCar(60, 'White-Blue', "Ford", True)
gaz = WorkCar(40, "Black", "Gaz", False)
porsche = SportCar(100, 'White', "Porsche", False)

print(f'{audi.show_speed()} на {audi.speed - 60}')
print(ford.police())
print(porsche.turn_left())
print(ford.color)


# ----5----
class Stationery:

	def __init__(self, title):
		self.title = title

	def draw(self):
		print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):

	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
	pass


class Hadle(Stationery):
	pass


pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Hadle('маркером')
pen.draw()
pencil.draw()
handle.draw()
