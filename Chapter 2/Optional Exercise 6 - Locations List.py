locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

print(len(locations)) # 6
print(sorted(locations)) # ['London', 'New York', 'amsterdam', 'dubai', 'paris', 'switzerland']
print(locations) # original order
print(sorted(locations, reverse = True)) #sorted no. 2 ['switzerland', 'paris', 'dubai', 'amsterdam', 'New York', 'London']
print(locations) #back to original order
locations.reverse() #make order reverse
print(locations) # now its reversed ['New York', 'amsterdam', 'London', 'switzerland', 'paris', 'dubai']
locations.sort()
print(locations) # now order is changed ['London', 'New York', 'amsterdam', 'dubai', 'paris', 'switzerland']
locations.sort(reverse=True) #['switzerland', 'paris', 'dubai', 'amsterdam', 'New York', 'London']
print(locations)