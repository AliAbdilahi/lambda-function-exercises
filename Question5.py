i = int(input("how many numbers:"))  
 

if i <= 0:  
   print("Enter number of pos")  
else:  
   print("Fibonacci numbers:")
   fibonacci= lambda i:  i if i <= 1 else fibonacci(i - 1) + fibonacci(i - 2);
   for x in range(i):  
       print(fibonacci(x))
   
