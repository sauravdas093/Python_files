# -*- coding: utf-8 -*-
"""Python_prime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zuKHRh_eSCLND1Ey-tzL50iAh91dQ29L
"""

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")