def factorial(num):  
   if num == 1:  
       return num
   else:#calling the recursion
       ans = num*factorial(num-1)  
       return ans
   
num = int(input("Enter a number to find its factorial: "))  
 
if num < 0:  
   print("Factorials doesn't exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print(f'The factorial of {num} is {factorial(num)}') 