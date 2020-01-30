import math,os

def bmi(height, weight):
	bmi = float(weight)/(float(height)**2) 
	# print("Your BMI is: {0} and you are ".format(bmi), end='')
	if ( bmi < 16.0):
		return ["severely underweight", str(bmi)]
	elif ( bmi >= 16.0 and bmi < 18.5):
		return ["underweight", str(bmi)]
	elif ( bmi >= 18.5 and bmi < 25):
		return ["Healthy", str(bmi)]
	elif ( bmi >= 25 and bmi < 30):
		return ["overweight", str(bmi)]
	elif ( bmi >=30):
		return ["severely overweight", str(bmi)]



def basal_metabolic_rate(height, weight, age, sex):		#to find out calorie needs
	if sex=="female":
		bmr = round((655.0+(4.35*float(weight))+(4.7*float(height))-(4.7*int(age))),2)
	else:
		bmr = round((66.0+( 6.23*float(weight))+( 12.7*float(height))-(6.8*int(age))),2)
	return str(bmr)
	


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
	


def waist_to_hip_ratio(waist, hip, sex):
	whr=round(float(waist)/float(hip),3)
	print("Your waist to hip ratio is "+str(whr))
	if sex=="female":
		if whr<0.80: 
			return ["You are at low health risk", str(whr)]
		elif whr>=0.80 and whr<=0.84: 
			return ["You are at moderate health risk", str(whr)]
		elif whr>=0.85: 
			return ["You are at high health risk", str(whr)]
	else:
		if whr<0.90: 
			return ["You are at low health risk", str(whr)]
		elif whr>=0.90 and whr<=0.99: 
			return ["You are at moderate health risk", str(whr)]
		elif whr>=1.00: 
			return ["You are at high health risk", str(whr)]




