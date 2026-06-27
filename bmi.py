# BMI (Body Mass Index) is a health metric that measures body fat based on a person's weight and height.
# Formula (Metric): BMI = weight (kg) / [height (m)]² (we will use this formula for our calculation)
# Formula (Imperial): BMI = (weight (lb) / [height (in)]²) * 703

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(bmi, "You are Underweight")
elif bmi <= 24.9:
    print(bmi, "You have a normal weight")
elif bmi <= 29.9:
    print(bmi, "You are overweight")
else:
    print(bmi, "You are obese")