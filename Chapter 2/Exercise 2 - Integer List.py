sample_list = [2,-1,50,0,122,5,69,192,420,22] #creating list of 10 list
print("The elements in the list are: ")
for list in sample_list: #print elements in sample list using for loop
    print(list, end=" ")

#Maximum and minimum in list
minimum = min(sample_list)
maximum = max(sample_list)
print("\nLowest number in list is: " + str(minimum))
print("Lowest number in list is: " + str(maximum))

sample_list.sort() # Ascending order
print('List in Ascending Order: ', sample_list)

sample_list.sort(reverse=True) # Descending order
print('List in Descending Order: ', sample_list)