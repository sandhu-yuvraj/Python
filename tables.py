# Tables and Multiples
n = int(input("Enter the number whose table you want to write: "))
m = int(input("Enter how many multiples you want to write: "))
for i in range (1, m+1) :
    print (n, "*", i, "=", n*i)