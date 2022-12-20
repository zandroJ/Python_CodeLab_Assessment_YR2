#Open the file bio.txt


f = open("bio.txt","w")
name = str(input("Name: " ))
age = int(input("Age: " ))
hometown = str(input("Hometown: " ))
f.write(f"Name: {name} \n")
f.write(f"Age: {str(age)} \n")
f.write(f"Hometown: {hometown} \n")
f.close()

f= open('bio.txt', "r+")
print("\nFollowing Data You Entered: ")
lines = f.readlines()



for each_line in lines:
 	print(each_line.rstrip())

