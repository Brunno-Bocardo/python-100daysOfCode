weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >=25:
    print("overweight")
elif bmi < 18.25:
    print("underweight")
else:
    print("normal weight")