import math,os

def bmi():
	height = float(input("Enter your height in meters: "))
	weight = float(input("Enter your weight in kg: "))
	bmi = weight/(height**2) 
	print("Your BMI is: {0} and you are ".format(bmi), end='')
	if ( bmi < 16):
		print("severely underweight")
	elif ( bmi >= 16 and bmi < 18.5):
		print("underweight")
	elif ( bmi >= 18.5 and bmi < 25):
		print("Healthy")
	elif ( bmi >= 25 and bmi < 30):
		print("overweight")
	elif ( bmi >=30):
		print("severely overweight")
	



def basal_metabolic_rate():		#to find out calorie needs
	height = float(input("Enter height in centimeters: "))
	weight = float(input("Enter weight in kg: "))
	age = float(input("Enter your age: "))
	sex = input("Enter your sex: ")
	if sex=="female":
		bmr = round((655.0+(4.35*weight)+(4.7*height)-(4.7*age)),2)
	else:
		bmr = round((66.0+( 6.23*weight)+( 12.7*height)-(6.8*age)),2)
	print("\nYour Basal Metabolic Rate is "+str(bmr)+" cal per day")
	


def calorie_needs():									#Harris Benedict Formula
	height = float(input("Enter height in centimeters: "))
	weight = float(input("Enter weight in kg: "))
	age = float(input("Enter your age: "))
	sex = input("Enter your sex: ")
	if sex=="female":
		bmr = round((655.0+(4.35*weight)+(4.7*height)-(4.7*age)),2)
	else:
		bmr = round((66.0+( 6.23*weight)+( 12.7*height)-(6.8*age)),2)
	print ("Types of lifestyle:\n1. 'sedentary': little or no exercise\n2. 'lightly active': light exercise/sports 1-3 days/week\n3. 'moderatetely active': moderate exercise/sports 3-5 days/week\n4. 'very active': hard exercise/sports 6-7 days a week\n5. 'extra active': very hard exercise/sports & physical job or 2x training")
	lifestyle={1:'sedentary',2:'lightly active',3:'moderatetely active',4:'very active',5:'extra active'}
	active=raw_input("Choose the number corresponding to your type of lifestyle : ")

	if active== '1': cal= bmr* 1.2
	elif active=='2': cal= bmr* 1.375
	elif active=='3': cal=bmr*1.55
	elif active=='4': cal=bmr* 1.725
	elif active=='5': cal=bmr*1.9
	else : calorie_needs()
	cal=round(cal,2)
	print("\nThe total number of calories you need in order to maintain your current weight : "+str(cal))
	if sex=="female":
		print("To lose weight, take "+str(cal-1200)+"-"+str(cal-500)+" calories a day\nTo gain weight, take "+str(cal+500)+" calories a day to gain one pound per week.")
	else:
		print("To lose weight, take "+str(cal-1800)+"-"+str(cal-500)+" calories a day\nTo gain weight, take "+str(cal+500)+" calories a day to gain one pound per week.")
	


def waist_to_hip_ratio():
	waist = float(input("Enter your waist measurement in cm: "))
	hip = float(input("Enter your hip measurement in cm: "))
	sex = input("Enter your sex: ")
	whr=round(float(waist)/hip,3)
	print("Your waist to hip ratio is "+str(whr))
	if sex=="female":
		if whr<0.80: print("\nYou are at low health risk")
		elif whr>=0.80 and whr<=0.84: print("\nYou are at moderate health risk")
		elif whr>=0.85: print("\nYou are at high health risk")
	else:
		if whr<0.90: print("\nYou are at low health risk")
		elif whr>=0.90 and whr<=0.99: print("\nYou are at moderate health risk")
		elif whr>=1.00: print("\nYou are at high health risk")




