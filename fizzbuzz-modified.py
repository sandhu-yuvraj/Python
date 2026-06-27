# The FizzBuzz problem is a classic programming interview challenge. 
# It requires writing a program that iterates through numbers up to a given limit. 
# For multiples of 3, it prints "Fizz",
# for multiples of 5, it prints "Buzz", 
# and for multiples of both, it prints "FizzBuzz"
n = int(input("Enter a number to end at: "))
for i in range(1 , n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
