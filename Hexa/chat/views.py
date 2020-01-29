from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def health_aspect(request):
    ans_bmi = ''
    ans_whr = ''
    if request.method == "POST":
        height = request.POST["height"]
        print(height)
        weight = request.POST["weight"]
        age = request.POST["age"]
        sex = request.POST["sex"]
        waist = request.POST["waist"]
        hip = request.POST["hip"]
        bmi = bmi(height,weight)
        if ( bmi < 16):
            ans_bmi+="severely underweight"
        elif ( bmi >= 16 and bmi < 18.5):
            ans_bmi+="underweight"
        elif ( bmi >= 18.5 and bmi < 25):
            ans_bmi+="Healthy"
        elif ( bmi >= 25 and bmi < 30):
            ans_bmi+="overweight"
        elif ( bmi >=30):
            ans_bmi+="severely overweight"
        bmr = basal_metabolic_rate(height,weight,age,sex)
        #cal = calorie_needs(height,weight,age,sex)
        #if sex=="female":
            #print("To lose weight, take "+str(cal-1200)+"-"+str(cal-500)+" calories a day\nTo gain weight, take "+str(cal+500)+" calories a day to gain one pound per week.")
        #else:
            #print("To lose weight, take "+str(cal-1800)+"-"+str(cal-500)+" calories a day\nTo gain weight, take "+str(cal+500)+" calories a day to gain one pound per week.")
        whr = waist_to_hip_ratio(waist,hip,sex)
        if sex=="female":
            if whr<0.80: ans_whr+="\nYou are at low health risk"
            elif whr>=0.80 and whr<=0.84: ans_whr+="\nYou are at moderate health risk"
            elif whr>=0.85: ans_whr+="\nYou are at high health risk"
        else:
            if whr<0.90: ans_whr+="\nYou are at low health risk"
            elif whr>=0.90 and whr<=0.99: ans_whr+="\nYou are at moderate health risk"
            elif whr>=1.00: ans_whr+="\nYou are at high health risk"
        context = {"ans_bmi":ans_bmi, "bmi":bmi, "bmr":bmr, "whr":whr, "ans_whr":ans_whr}
        return render(request, 'chat/bmi.html', context)
        
import math,os

def bmi(height,weight):
	height /= 100
	bmi = weight/(height**2) 
	#print("Your BMI is: {0} and you are ".format(bmi), end='')

	return bmi	



def basal_metabolic_rate(height,weight,age,sex):		#to find out calorie needs
	if sex=="female":
		bmr = round((655.0+(4.35*weight)+(4.7*height)-(4.7*age)),2)
	else:
		bmr = round((66.0+( 6.23*weight)+( 12.7*height)-(6.8*age)),2)
	#print("\nYour Basal Metabolic Rate is "+str(bmr)+" cal per day")
	return bmr
	


def calorie_needs(height,weight,age,sex):
	if sex=="female":
		bmr = round((655.0+(4.35*weight)+(4.7*height)-(4.7*age)),2)
	else:
		bmr = round((66.0+( 6.23*weight)+( 12.7*height)-(6.8*age)),2)
	#print ("Types of lifestyle:\n1. 'sedentary': little or no exercise\n2. 'lightly active': light exercise/sports 1-3 days/week\n3. 'moderatetely active': moderate exercise/sports 3-5 days/week\n4. 'very active': hard exercise/sports 6-7 days a week\n5. 'extra active': very hard exercise/sports & physical job or 2x training")
	lifestyle={1:'sedentary',2:'lightly active',3:'moderatetely active',4:'very active',5:'extra active'}
	active=raw_input("Choose the number corresponding to your type of lifestyle : ")

	if active== '1': cal= bmr* 1.2
	elif active=='2': cal= bmr* 1.375
	elif active=='3': cal=bmr*1.55
	elif active=='4': cal=bmr* 1.725
	elif active=='5': cal=bmr*1.9
	else : calorie_needs()
	cal=round(cal,2)
	#print("\nThe total number of calories you need in order to maintain your current weight : "+str(cal))
	
	return cal


def waist_to_hip_ratio(waist,hip,sex):
	whr=round(float(waist)/hip,3)
	#print("Your waist to hip ratio is "+str(whr))
	
	return whr




