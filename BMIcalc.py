def calculate_bmi(Weight, Height):
    BMI = 703* (Weight / (Height*Height))

    if BMI>= 30:
        print ('You are {}'.format(BMI))
        print ('Obese')

    elif BMI>= 25 and BMI< 29.9:
        print ('You are {}'.format(BMI))
        print ('Overweight')

    elif BMI>= 18.5 and BMI<24.9:
        print ('You are {}'.format(BMI))
        print ('Normal Weight')

    else: 
        print ('You are{}'.format(BMI))
        print ('Underweight')

Weight = (input ('What is your weight?'))
Height = (input ('What is your height?'))
Weight = float(Weight)
Height = float(Height)

calculate_bmi (Weight, Height)