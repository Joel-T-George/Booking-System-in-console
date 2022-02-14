#JSON DATA
import json

class BookingSystem :
	def __init__(self,person_name,person_email,menucard):
		self.person = person_name
		self.email = person_email
		self.ordereditems = []
		self.Dishes = menucard
		self.wishinghim()
		
		
	def wishinghim(self):
		print("\n -*-*-*-*-*-*-*-*-*-welcome to kojo restaurant-*-*-*-*-*-*-*-*-*- \n \n hey,"+self.person )
		self.showMenucard()
		self.dishSelector()

	def showMenucard(self):
		print("\n Below see our restaurant -*-*-Menucard-*-*- \n" )
		count=0
		#table header printing line here 
		print("________________________________________________ \n Sno --*-- Items--------*-- Price")
		for Dish in self.Dishes:
			print(" ",count+1," --*-- ",Dish["Items"],"--------*-- ",Dish["Rs"])	
			count+=1
		print("________________________________________________ \n above seen menucard from 'Sno' you can place your order \n exit- type 'E' \n select dishes - type 'S' \n to complete order - press 'K'")
	def dishSelector(self):
		waitStillSay = True
		while waitStillSay:
			customer_decision = input("*****Enter your Choice: ")
			if customer_decision == "E" or customer_decision == "e" :
				self.editList()
			elif customer_decision == "S" or customer_decision == "s" :
				self.selectDishes()
			elif customer_decision == "K" or customer_decision == "k" :
				if self.toCompleteOrder() == True :
					self.finalSltDishs()
					waitStillSay = False
				
					
					
			
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
				self.ordereditems.pop(editKey-1)
				print("sucessfully deleted! \n_______________________________________")

	def selectDishes(self):
		for orderItem in self.ordereditems:
			print(orderItem)
		print("_______________________________________ \n Select your Dish \n_______________________________________")
		sltDishId=int(input("Enter your item Sno : "))
		if sltDishId <= len(self.Dishes):
			selDish = self.Dishes[sltDishId-1]	
			quantity = int(input("Enter your Quantity of Dish: "))
			selDish["Quantity"]= quantity
			self.ordereditems.append(selDish)
			print("sucessfully registered \n_______________________________________")
		
		else:
			print("Invalid Item")	
		
	def toCompleteOrder(self):
		print("Are you sure to Complete Orders! \n if want to Complete type --'Y' \n if wish to continue to type--'N'")
		confirmation = input("Type you decison: ")
		if confirmation == "Y" or confirmation == "y":
			print("Orders are registered!")
			return True
		if confirmation == "N" or confirmation == "n":
			return False
	def finalSltDishs(self):
		count=0
		print("________________________________________________ \n Sno --*-- Items--------*-- Price -------*-- Quantity")
		for orderItem in self.ordereditems:
			
			S,Is,Pe,Qy = str(count+1),orderItem["Items"],str(orderItem["Rs"]),str(orderItem["Quantity"])
			print(" "+S+" --*-- "+Is+"--------*-- "+Pe+"rs -------*-- "+Qy+"-Qty")	
			count+=1

			
	
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




	