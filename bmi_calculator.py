print(" ")
print("\t\t\tBMI Calculator")
print("\t\t\tMade by Daniel Chen")
print(" ")
print(" ")



weight = input("What is your weight in pounds?  ")
height = input("What is your height in inches?  ")
bmi = (weight * 703) / (height * height)
bmi1 = str(bmi)
print ("Your BMI is " +bmi1)

if bmi1 < 18.5:
	type = str("underweight")
if 18.5 <= bmi1 > 25:
	type = str("normal")
if 25 <= bmi1 > 30:
	type = str("overweight")
if bmi1 < 30:
	type = ("obese")
	
print("You are " + type)

if type = obese or overweight
	print("Try losing some weight")
if type = underweight
	print("Try gaining some weight")
if type = normal
	print("You are good")