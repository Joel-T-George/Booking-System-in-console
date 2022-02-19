
import json
from datetime import datetime
import smtplib
import random
from email.message import EmailMessage
#app logic and function codes are in the class of booking system
class BookingSystem :
	def __init__(self,person_name,person_email,menucard):
		self.person = person_name
		self.email = person_email
		self.ordereditems = []
		self.Dishes = menucard
		self.wishinghim()
		
	# intro show in cmd line welcoming customer	
	def wishinghim(self):
		print("\n -*-*-*-*-*-*-*-*-*-welcome to kojo restaurant-*-*-*-*-*-*-*-*-*- \n \n hey,"+self.person )
		self.showMenucard()
		self.dishSelector()

	# Showing menucard ordering starts..
	def showMenucard(self):
		print("\n Below see our restaurant -*-*-Menucard-*-*- \n" )
		count=0
		#table header printing line here 
		print("________________________________________________ \n Sno --*-- Items--------*-- Price")
		for Dish in self.Dishes:
			print(" ",count+1," --*-- ",Dish["Items"],"--------*-- ",Dish["Rs"])	
			count+=1
		print("________________________________________________ \n above seen menucard from 'Sno' you can place your order \n exit- type 'E' \n select dishes - type 'S' \n to complete order - press 'K'")
	
	# home functions to ordering ,editing,and complete ordering
	def dishSelector(self):
		waitStillSay = True
		while waitStillSay:
			print("current total: "+str(self.currentRateItems())+"rs")
			customer_decision = input("*****Enter your Choice: ")
			if customer_decision == "E" or customer_decision == "e" :
				self.editList()
			elif customer_decision == "S" or customer_decision == "s" :
				self.selectDishes()
			elif customer_decision == "K" or customer_decision == "k" :
				if self.toCompleteOrder() == True :
					self.finalSltDishs()
					waitStillSay = False
				
	# Edit option after ordered items and any corrections		
	def editList(self):
		#Showing ordered Items this codes.
		for orderItem in self.ordereditems:
			print(orderItem)
		print("_______________________________________ \n editor is on \n _______________________________________")
		editKey = int(input("Enter your want to edit Serial No: "))
		if editKey <= len(self.ordereditems):
			print("if you want to delete item type--'D' \n if you want to edit quality of item type-- 'Q'")
			choice = input("Type your Choice: ")
			if choice == "D" or choice == "d" :
				self.ordereditems.pop(editKey-1)
				print("sucessfully deleted!")
			if choice == "Q" or choice == "q" :
				quantity = int(input("Enter your Change Quantity of Dish: "))
				self.ordereditems[editKey-1]["Quantity"]=quantity 
				
				print("sucessfully changed Quantity! \n_______________________________________")


	# Select Dishes by serial number , ordering and mentioning quantiy.
	def selectDishes(self):
		for orderItem in self.ordereditems:
			print(orderItem)
		print("_______________________________________ \n Select your Dish \n_______________________________________")

		try :
			sltDishId=int(input("Enter your item Sno : "))
			
		except ValueError:
			print("Please enter number not a word!")
			sltDishId=int(input("Enter your item Sno : "))

		if sltDishId <= len(self.Dishes):
			selDish = self.Dishes[sltDishId-1]
			try :
				quantity = int(input("Enter your Quantity of Dish: "))
			
			except ValueError:
				print("Please enter number not a word!")
				quantity = int(input("Enter your Quantity of Dish: "))	
			
			selDish["Quantity"]= quantity
			self.ordereditems.append(selDish)
			print("sucessfully registered \n_______________________________________")
		
		else:
			print("Invalid Item")	

	#It output gives current list ordered price
	def currentRateItems(self):
		total=0
		for items in self.ordereditems:
			peritem = items["Rs"]*items["Quantity"]
			total+= peritem
		return total

	# completing of order items and send to final process of billing 
	def toCompleteOrder(self):
		print("Are you sure to Complete Orders! \n if want to Complete type --'Y' \n if wish to continue to type--'N'")
		confirmation = input("Type you decison: ")
		if confirmation == "Y" or confirmation == "y":
			print("Orders are registered!")
			return True
		if confirmation == "N" or confirmation == "n":
			return False

	# Editing frist entered mail and it will otp autheication process
	def editEmail(self):
		print("_______________________________________ \n Edit email ID \n_________________________________")
		changeEmail = input("Enter your new Email ID: ")
		Otp = genOtp()
		message = "it is your OTP: "+str(Otp)
		sender(changeEmail,"verification for change new email ID",message) 
		verify =input("Enter you Otp number recieved in mail: " )
		if verify == Otp:
			self.email = changeEmail

	# Final showing of ordered list and here can delete items and go to email process
	def finalSltDishs(self):
		count=0
		print("________________________________________________ \n Sno --*-- Items--------*-- Price -------*-- Quantity")
		for orderItem in self.ordereditems:
			
			S,Is,Pe,Qy = str(count+1),orderItem["Items"],str(orderItem["Rs"]),str(orderItem["Quantity"])
			print(" "+S+" --*-- "+Is+"--------*-- "+Pe+"rs -------*-- "+Qy+"-Qty")	
			count+=1
		print("********* total amount:"+str(self.currentRateItems())+"rs ******")
		waittoconfirm = True
		while waittoconfirm:
			print("_____________________________________________________\n please confirm your email ID '"+self.email+"' because in mail only receive bill and payment option. \n For edit email id type--'M' \n For edit your items type--'E' \n Show Ordered list again type--'S' \n Confirm Your final Order type--'O' ")
			choice = input("Enter your deal: ")
			if choice == "M" or choice == "m":
				self.editEmail()
			elif choice == "E" or choice == "e":
				self.editList()
			elif choice == "O" or choice == "o":
				self.finalisedItems()
				waittoconfirm =False
			elif choice =="S" or choice =="s":
				count =0
				for orderItem in self.ordereditems:
					S,Is,Pe,Qy = str(count+1),orderItem["Items"],str(orderItem["Rs"]),str(orderItem["Quantity"])
					print(" "+S+" --*-- "+Is+"--------*-- "+Pe+"rs -------*-- "+Qy+"-Qty")	
					count+=1
				print("total price: "+str(self.currentRateItems())+"rs")
			elif choice == "D" or choice == "d":
				exit()

# 6 digit number random generate 					
def genOtp():
	val =""
	for i in range(0,6):
		ran=random.randrange(0, 10)
		val+=str(ran)
		
	return val
# mail  sender option
def sender( to_mail,subject,messages):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('hostemail','enter_your_apikey')
    emails = EmailMessage()
    emails['From'] =  'hostemail'
    emails['To'] = to_mail
    emails['Subject'] = subject
    emails.set_content(messages)
    server.send_message(emails)		



#inital code runs.....	
print("\n ************Welcome to online booking system************\n \n if you want to order food \n \n *want to order -- type 'y' \n *quit -- type 'n'")

gateQuestion  = input(" \n type your next step: ")
with open('menucard.json') as json_file:
    Dishes = json.load(json_file)
if gateQuestion == "y" or gateQuestion == "Y" :
	print("\n ------------------------------------------")
	name = input("Enter your sweet name: ")
	email  = input("Enter your email id: ")
	customer = BookingSystem(name,email,Dishes)
	
	
elif gateQuestion == "n" or gateQuestion == "N" :
	exit()

#emergency quit show off..
try:
	raise KeyboardInterrupt
finally:
	print('Thankyou for emergency exiting')



	