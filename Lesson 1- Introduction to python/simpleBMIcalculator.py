print('Hi, I am your BMI Calculator. Follow the instructions below to calculate your BMI')

name = str(input("Please enter your name: "))
print('Please enter your height in metre')
height = float(input("Height in metre:"))
print('Please enter your weight in kilogram')
weight = float(input("Weight in kilogram:"))
BMI = (weight/(height**2))
print('Thank you for the inputs ' + name + ' Your BMI is', (BMI))

print('Press 1 to know your category or press 2 to exust')

category = input()
if category == '1':
    print('Lets know what category you fall into')
    if BMI < 16.5:
        print('You are severely underweight')
    elif BMI > 16.5 and BMI < 18.5:
        print('You are underweight')
    elif BMI > 18.5 and BMI < 25:
        print('You are normal')
    elif BMI > 25 and BMI < 30:
        print('You are overweight')
    elif BMI > 30 and BMI < 35:
        print('You are obese class 1') 
    elif BMI > 35 and BMI < 40:
        print('You are obese class 2')  
    elif BMI > 40 and BMI < 45:
        print('You are severely obese') 
    elif BMI > 45 and BMI < 50:
        print('You are morbidly obese')
    elif BMI > 50 and BMI < 60:
        print('You are super obese') 
    elif BMI > 60:
        print('You are hyper obese')           
else:
    print('Thank you for using the calculator')
