print("\n\t\t\tBMI Calculator\n\t\t\tMade by Daniel Chen\n\n")
bmi=(int(input("What is your weight in pounds?  "))*703)/(int(input("What is your height in inches?  "))**2)
t="underweight"if bmi<18.5 else"normal"if bmi<25 else"overweight"if bmi<30 else"obese"
print("Your BMI is "+str(bmi)+"\nYou are "+t)
print("Try losing some weight"if t=="obese"or t=="overweight"else"You are good"if t=="normal"else"Try gaining some weight")
