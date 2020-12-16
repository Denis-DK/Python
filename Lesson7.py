# ----------------------------------1----------------------------

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class Matrix:
	def __init__(self, list_1):
		self.list_1 = list_1

	def __str__(self):
		return "\n" .join(map(str, self.list_1))

	def __add__(self, other):
		c = []
		for i in range(len(self.list_1)):
			c.append([])
			for j in range(len(self.list_1[0])):
				c[i].append(self.list_1[i][j] + other.list_1[i][j])
		return "\n" .join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(matrix_1 + matrix_2)


# ----------------------------------2----------------------------
from abc import ABC, abstractmethod


class Clothes(ABC):
	def __init__(self, param):
		self.param = param

	@property
	@abstractmethod
	def concept(self):
		pass

	def __add__(self, other):
		return self.concept + other.concept


class Coat(Clothes):
	@property
	def concept(self):
		print(f"{round(self.param / 6.5) + 0.5}")
		return round(self.param / 6.5) + 0.5


class Suit(Clothes):
	@property
	def concept(self):
		print(f'{round(2 * self.param + 3) / 100}')
		return (2 * self.param + 3) / 100


coat = Coat(42)
suit = Suit(170)
print(coat + suit)

# ----------------------------------3----------------------------


class Cell:
	def __init__(self, nums):
		self.nums = nums

	def make_order(self, rows):
		return "\n".join(["*" * rows for _ in range(self.nums // rows)]) + "\n" + "*" * (self.nums % rows)

	def __str__(self):
		return self.nums

	def __add__(self, other):
		return f"Сумма: {self.nums + other.nums}"

	def __sub__(self, other):
		return self.nums - other.nums if self.nums - other.nums > 0 \
			else "Невозможно!"

	def __mul__(self, other):
		return f"{self.nums * other.nums}"

	def __floordiv__(self, other):
		return f" {self.nums // other.nums}"


cells1 = Cell(13)
cells2 = Cell(25)

print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 // cells2)
