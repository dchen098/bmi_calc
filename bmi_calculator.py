print(" ")
print("\t\t\tBMI Calculator")
print("\t\t\tMade by Daniel Chen")
print(" ")
print(" ")

#daniel ur so stupid

weight = input("What is your weight in pounds?  ")
height = input("What is your height in inches?  ")
bmi = (weight * 703) / (height * height)
print ("Your BMI is " + str(bmi))

if bmi < 18.5:
	type = "underweight"
if 18.5 <= bmi < 25:
	type = "normal"
if 25 <= bmi < 30:
	type = "overweight"
if bmi < 30:
	type = "obese"
	
print("You are " + type)

if type == "obese" or type == "overweight":
	print("Try losing some weight")
if type == "underweight":
	print("Try gaining some weight")
if type == "normal":
	print("You are good")
