import statistics
with open("petrolPrice.txt", "r") as f:
	lines = f.readlines()
	liters = []
	cost = []
	petrolData= [i.split() for i in lines]
	for l in lines:
		data = l.split()
		liters.append((data[0]))
		cost.append((data[1]))

my_int = 7

#convert string list to int
convert_liter = [eval(i) for i in liters] 
convert_cost = [eval(i) for i in cost]  

per_liter = [i / j for i, j in zip(convert_cost, convert_liter)]
avg = sum(per_liter) / len(convert_cost)


print(f'PETROL DATA: {petrolData}')
#What was the overall average price per litre of petrol bought?
print(f'\nOverall avg price per litres bought: {avg}') 
#How much petrol in litres was bought at under 3.5AED per liter?
print(per_liter)