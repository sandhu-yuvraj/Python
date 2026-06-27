# The FizzBuzz problem is a classic programming interview challenge. 
# It requires writing a program that iterates through numbers up to a given limit. 
# For multiples of 3, it prints "Fizz",
# for multiples of 5, it prints "Buzz", 
# and for multiples of both, it prints "FizzBuzz"
number = int(input("Enter a number: "))
if (number%3 == 0) and (number%5 == 0):
    print("Divisible by both 3 and 5 , FizzBuzz")
elif (number%3 == 0):
    print("Divisible by 3 , Fizz")
elif (number%5 == 0):
    print("Divisible by 5 , Buzz") 
else:
    print("Not divisible by 3 or 5")
