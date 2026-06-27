number = int(input("Enter a number: "))
if (number%3 == 0) and (number%5 == 0):
    print("Divisible by both 3 and 5 , FizzBuzz")
elif (number%3 == 0):
    print("Divisible by 3 , Fizz")
elif (number%5 == 0):
    print("Divisible by 5 , Buzz") 
else:
    print("Not divisible by 3 or 5")