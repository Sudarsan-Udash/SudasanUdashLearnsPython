print('Hi, I am your BMI Calculator. Follow the instructions below to calculate your BMI')

name = str(input("Please enter your name: "))
print('Please enter your height in metre')
height = int(input("Height in metre:"))
print('Please enter your weight in kilogram')
weight = int(input("Weight in kilogram:"))
BMI = (weight/(height**2))
print('Thank you for the inputs ' + name + ' Your BMI is', (BMI))

print('We will soon update you with your body status')
