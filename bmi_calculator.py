print(" ")
print("\t\t\tBMI Calculator")
print("\t\t\tMade by Daniel Chen")
print(" ")
print(" ")

#daniel ur so stupid

weight = int(input("What is your weight in pounds?  "))
height = int(input("What is your height in inches?  "))
bmi = (weight * 703) / (height * height)
print ("Your BMI is " + str(bmi))

if bmi < 18.5:
	type = "underweight"
elif bmi < 25:
	type = "normal"
elif bmi < 30:
	type = "overweight"
else:
	type = "obese"
	
print("You are " + type)

if type == "obese" or type == "overweight":
	print("Try losing some weight")
if type == "underweight":
	print("Try gaining some weight")
if type == "normal":
	print("You are good")
