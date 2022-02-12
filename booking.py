#JSON DATA
Dishes=[{"Items":"POROTTA","Rs":10},{"Items":"CHAPATTI","Rs":8},{"Items":"IDLY","Rs":5},{"Items":"DOSA" ,"Rs":9},{"Items":"PONGAL","Rs":5},{"Items":"CHICKEN BRIYANI","Rs":100},{"Items":"MUTTON BRIYANI","Rs":150},{"Items":"FISH BRIYANI","Rs":125},{"Items":"CHICKEN TIKKA","Rs":90},{"Items":"FRIED RICE","Rs":100},{"Items":"VEG PULAO","Rs":80},{"Items":"EGG RICE","Rs":70}]
class BookingSystem :
	def __init__(self,person_name,person_email):
		self.person = person_name
		self.email = person_email
		self.wishinghim()
		self.orderedItems = []
		
	def wishinghim(self):
		print("\n -*-*-*-*-*-*-*-*-*-welcome to kojo restaurant-*-*-*-*-*-*-*-*-*- \n \n hey,"+self.person )
		self.showMenucard()
		self.dishSelector()

	def showMenucard(self):
		print("\n Below see our restaurant -*-*-Menucard-*-*- \n" )
		count=0
		#table header printing line here 
		print("________________________________________________ \n Sno --*-- Items--------*-- Price")
		for Dish in Dishes:
			print(" ",count+1," --*-- ",Dish["Items"],"--------*-- ",Dish["Rs"])	
			count+=1
		print("________________________________________________ \n above seen menucard from 'Sno' you can place your order \n exit- type 'E' \n select dishes - type 'S' \n to complete order - press 'K'")
	def dishSelector(self):
		waitStillSay = false
		

			
	
print("\n ************Welcome to online booking system************\n \n if you want to order food \n \n *want to order -- type 'y' \n *quit -- type 'n'")

gateQuestion  = input(" \n type your next step: ")

if gateQuestion == "y" or gateQuestion == "Y" :
	print("\n ------------------------------------------")
	name = input("Enter your sweet name: ")
	phone  = input("Enter your email id: ")
	customer = BookingSystem(name,phone)
	
	
elif gateQuestion == "n" or gateQuestion == "N" :
	exit()




	