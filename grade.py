#Take marks as input and grade the student based on the marks obtained
marks = int(input("Enter the marks obtained: "))
if marks >= 90:
    print("Grade: A")  
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")  
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")