from functools import reduce


def my_list(num_1, num_2):
	return num_1 * num_2


my_new_list = [num for num in range(100, 1001, 2)]
print(f" {my_new_list} \n {reduce(my_list, my_new_list)}")
