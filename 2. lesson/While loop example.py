investment = 1000
GOAL = 2000
interest_rate = 0.07
years=0
while investment < GOAL:
    years += 1 # += is shorthand for years = years + 1
    investment = investment * (1 + interest_rate)
else: 
    print(years)