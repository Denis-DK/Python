from sys import argv

name, rate_per_hour, productivity, bonus = argv
rate_per_hour = int(rate_per_hour)
productivity = int(productivity)
bonus = int(bonus)
result = productivity * rate_per_hour + bonus

print(f"Заработная плата: {result}")
