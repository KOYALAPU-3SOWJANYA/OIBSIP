name = input("Hi, What's your name?")
height = float(input("What's your height? (In metres)"))
weight = float(input("What's your weight? (In kg)"))
height = height * height
BMI = weight/height
'''
 If the person's BMI is below 18.5 then he is underweight
Or if the person's BMI is between 18.5 and 24.9 then the person's BMI is normal
Or if the person's BMI is above 24.9 then the person is overweight'''
if BMI < 18.5:
 print(name + " is underweight\n")
elif BMI <= 24.9:
 print(name + " is normal")
else:
 print(name + " is overweight")