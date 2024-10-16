weight = float(input())
height = float(input())

bmi = weight / (height ** 2)
print(bmi)

# Conditions have been corrected
if bmi >= 30:
    print('Obesity')
elif 25 <= bmi < 30:
    print('Overweight')
elif 18.5 <= bmi < 25:
    print('Normal')
elif bmi < 18.5:
    print('Underweight')

# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more