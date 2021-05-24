import random
random.seed(100)
#****INSTRUCTIONS FOR LAB 06: OOP****
#Read all instructions in the comments before doing the lab.
#Look at the tests first to understand how the methods are supposed to behave.
#Remember, you can run your code inside of Sublime:
#Press Ctrl+B for Windows
#Press Cmd+B for Mac

def randAlphaNumeric():
	return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

class Vehicle(object):
	#Vehicle class
	#Add static variables here
	registeredVehicles = []
	registeredVehiclePlates = []

	def __eq__(self, other):
		#look up documemntation for this method online to learn more about how to use it
		#two vehicles are equal if their vins are the same
		return self.vin == other.vin
		 

	def __init__(self, make, model, year, price):
		#when a vehicle is created, it also gets a 12 character/number string
		#called a vin created using the randAlphaNumeric function above
		self.make = make
		self.model = model
		self.year = year
		self.price = float(price)
		self.owner = None
		self.licenseplate = None		
		self.vin = randAlphaNumeric() +  randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() 


	def checkInfo(self):
		#this method should return a tuple of a car's make, model, year, vin, price, owner name, and license plate.
		#If the car is unpurchased, the license plate and owner should be None.
		if self.owner == None:
			return (self.make, self.model, self.year, self.vin, self.price, None, None)
		else:
			return (self.make, self.model, self.year, self.vin, self.price, self.owner.name(), self.licenseplate)


	def accident(self, otherVehicle):
		#when two vehicles are in an accident, both of their prices decrease by 75%		
		self.price = self.price - (self.price * 0.75)	
		otherVehicle.price = otherVehicle.price - (otherVehicle.price * 0.75)


	def purchased(self, owner):
		#When purchased, the owner becomes the new owner of the vehicle, the price decreases by half
		#Use the transfer ownership function to move the car from the old owner's list, if one exists, to the new owner's list 
		#If no license plate has been assigned, use the randAlphaNumeric function above to generate a new 7 character/number
		#string for the plate.This function should return a string of: "owner, license_plate"
			# 1. decrease the price
		self.price = self.price - (self.price/2)
			# 2. move car's previous owner to new owner
		if self.owner != None:
			owner.transferCar(self.owner, self)
		self.owner = owner
			# 3. license plate
		if self.licenseplate == None:
			self.licenseplate = randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric()
			Vehicle.registeredVehiclePlates.append(self.licenseplate)
			Vehicle.registeredVehicles.append(self)
		return self.owner.name() + ", " + self.licenseplate


	@staticmethod
	def allRegisteredVehicles():
		#returns a list of all registered vehicles (aka vehicles that have been purchased and have a license plate)
		return Vehicle.registeredVehicles

	@staticmethod
	def allRegisteredVehiclePlates():
		#returns a list of all registered vehicles' license plates
		return Vehicle.registeredVehiclePlates


class Driver(object):
	#Driver class
	#Add static variables here
	

	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
		self.driverID = None
		self.garage = []


	def name(self):
		#return a string concatenating firstName and lastName with a space
		return self.firstName + " " + self.lastName


	def drivingExam(self):
		#When a Driver takes a drivingExam, they get a driverID of an
		#8 character/number string using the randAlphaNumeric function above
		#this function should return the new driverID
		self.driverID = randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric() + randAlphaNumeric()
		return self.driverID

	def checkInfo(self):
		#returns a tuple listing a driver's info: (first_name, last_name, driver_id)
		#if the driver does has not passed their driving exam yet, it returns:
		#(first_name, last_name, None)
		return (self.firstName, self.lastName, self.driverID)
		

	def ownedCars(self):
		#return a list of the driver's owned cars 
		# WHOLE VEHICLE
		return self.garage

	def purchaseCar(self, vehicle):
		#purchase a vehicle using the purchased function from the Vehicle class
		# 1. tell owner that is has a car
		self.garage.append (vehicle)
		# 2. tell car that it has an owner	
		vehicle.purchased(self)


	def transferCar(self, previousOwner, vehicle):
		#move this car from the previous owner's list to this driver's list
		#if the previousOwner was None, then simply add it to the new owner's list		
		if vehicle.owner == None:
			self.garage.append(vehicle)
		else:
			self.garage.append(vehicle)
			previousOwner.garage.remove(vehicle)


#Vehicle construction
car1 = Vehicle("Fiat", "500e", 2013, 33000)
car2 = Vehicle("Aprilia", "Mana 850", 2011, 12000)
car3 = Vehicle("Toyota", "Highlander", 2016, 31000)
car4 = Vehicle("Tesla", "S", 2017, 68000)
car5 = Vehicle("BMW", "7", 2018, 83000)
car6 = Vehicle("Toyota", "Highlander", 2016, 31000)
# assert(car1.checkInfo() == ('Fiat', '500e', 2013, 'J33LZW16H8HF', 33000, None, None))
assert(car1.checkInfo() == ('Fiat', '500e', 2013, car1.vin, 33000, None, None))
# assert(car3.checkInfo() == ('Toyota', 'Highlander', 2016, 'X0NZ39RYKHLA', 31000, None, None))
assert(car3.checkInfo() == ('Toyota', 'Highlander', 2016, car3.vin, 31000, None, None))
assert(len(Vehicle.allRegisteredVehiclePlates()) == 0)

#Driver construction
person1 = Driver('The', 'Stig')
person2 = Driver('Matt', 'LeBlanc')
person3 = Driver('Richard', 'Hammond')
person4 = Driver('James', 'May')
person5 = Driver('Jeremy', 'Clarkson')
assert(person1.checkInfo() == ('The', 'Stig', None))
assert(person2.name() == "Matt LeBlanc")

#Driving exam method
person3.drivingExam()
person5.drivingExam()
# assert(person3.checkInfo() == ('Richard', 'Hammond', 'DRHDOT7N'))
assert(person3.checkInfo() == ('Richard', 'Hammond', person3.driverID))
# assert(person5.checkInfo() == ('Jeremy', 'Clarkson', 'WV3AH4M7'))
assert(person5.checkInfo() == ('Jeremy', 'Clarkson', person5.driverID))

#Purchase methods
person1.purchaseCar(car1)
person3.purchaseCar(car3)
person3.purchaseCar(car4)
person3.purchaseCar(car6)
person5.purchaseCar(car5)
person5.purchaseCar(car2)

print (car1.checkInfo())

#assert(car1.checkInfo() == ('Fiat', '500e', 2013, 'J33LZW16H8HF', 16500.0, 'The Stig', 'HNCYGZJ'))
assert(car1.checkInfo() == ('Fiat', '500e', 2013, car1.vin, 16500.0, 'The Stig', car1.licenseplate))
# assert(person3.ownedCars()[0].checkInfo() == ('Toyota', 'Highlander', 2016, 'X0NZ39RYKHLA', 15500.0, 'Richard Hammond', '48C2KD4'))
assert(person3.ownedCars()[0].checkInfo() == ('Toyota', 'Highlander', 2016, person3.ownedCars()[0].vin, 15500.0, 'Richard Hammond', person3.ownedCars()[0].licenseplate))
# assert(person3.ownedCars()[1].checkInfo() == ('Tesla', 'S', 2017, 'ZJKMKBP2YI9D', 34000.0, 'Richard Hammond', 'DMPKGCI'))
assert(person3.ownedCars()[1].checkInfo() == ('Tesla', 'S', 2017, person3.ownedCars()[1].vin, 34000.0, 'Richard Hammond', person3.ownedCars()[1].licenseplate))
# assert(person3.ownedCars()[2].checkInfo() == ('Toyota', 'Highlander', 2016, 'T1QP165QJDUK', 15500.0, 'Richard Hammond', 'NFHQEZC'))
assert(person3.ownedCars()[2].checkInfo() == ('Toyota', 'Highlander', 2016, person3.ownedCars()[2].vin, 15500.0, 'Richard Hammond', person3.ownedCars()[2].licenseplate))

#Registered Vehicles methods
# assert(tuple(Vehicle.allRegisteredVehiclePlates()) == tuple(['HNCYGZJ', '48C2KD4', 'DMPKGCI', 'NFHQEZC', '8142V37', 'MQ0JN0E']))
assert(tuple(Vehicle.allRegisteredVehiclePlates()) == tuple([Vehicle.allRegisteredVehiclePlates()[0], Vehicle.allRegisteredVehiclePlates()[1], 
	Vehicle.allRegisteredVehiclePlates()[2], Vehicle.allRegisteredVehiclePlates()[3], Vehicle.allRegisteredVehiclePlates()[4], Vehicle.allRegisteredVehiclePlates()[5]]))
assert(Vehicle.allRegisteredVehicles()[1].checkInfo() == ('Toyota', 'Highlander', 2016, Vehicle.allRegisteredVehicles()[1].vin, 15500.0, 'Richard Hammond', 
	Vehicle.allRegisteredVehicles()[1].licenseplate))

#Transfer ownership methods
person5.purchaseCar(car6)
person2.purchaseCar(car1)
# assert(person3.ownedCars()[0].checkInfo() == ('Toyota', 'Highlander', 2016, 'X0NZ39RYKHLA', 15500.0, 'Richard Hammond', '48C2KD4'))
assert(person3.ownedCars()[0].checkInfo() == ('Toyota', 'Highlander', 2016, person3.ownedCars()[0].vin, 15500.0, 'Richard Hammond', person3.ownedCars()[0].licenseplate))
assert(len(person3.ownedCars()) == 2)
# assert(person5.ownedCars()[2].checkInfo() == ('Toyota', 'Highlander', 2016, 'T1QP165QJDUK', 7750.0, 'Jeremy Clarkson', 'NFHQEZC'))
assert(person5.ownedCars()[2].checkInfo() == ('Toyota', 'Highlander', 2016, person5.ownedCars()[2].vin, 7750.0, 'Jeremy Clarkson', person5.ownedCars()[2].licenseplate))
# assert(car6.checkInfo() == ('Toyota', 'Highlander', 2016, 'T1QP165QJDUK', 7750.0, 'Jeremy Clarkson', 'NFHQEZC'))
assert(car6.checkInfo() == ('Toyota', 'Highlander', 2016, car6.vin, 7750.0, 'Jeremy Clarkson', car6.licenseplate))

#Accidents method
car3.accident(car4)
# assert(car3.checkInfo() == ('Toyota', 'Highlander', 2016, 'X0NZ39RYKHLA', 3875.0, 'Richard Hammond', '48C2KD4'))
assert(car3.checkInfo() == ('Toyota', 'Highlander', 2016, car3.vin, 3875.0, 'Richard Hammond', car3.licenseplate))
# assert(car4.checkInfo() == ('Tesla', 'S', 2017, 'ZJKMKBP2YI9D', 8500.0, 'Richard Hammond', 'DMPKGCI'))
assert(car4.checkInfo() == ('Tesla', 'S', 2017, car4.vin, 8500.0, 'Richard Hammond', car4.licenseplate))