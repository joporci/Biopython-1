class Car:
	brand=None
	model=None
    	year=None
    	price = None
	num_plate = None

	
    	def __init__(self, brand, model, year, price, num_plate):
        	self.brand = brand
        	self.model = model
        	self.year  = year
		self.price = price
		self.price = num_plate
        
   	def toString(self):
        	return "BRAND: "+self.brand+"\nMODEL: "+self.model+"\nYEAR: "+str(self.year)+"\nPRICE: "+self.year+'\nNUMBER-PLATE: '+self.num_plate


class Bakkie(Car):
	capacity=None
	
	def __init__(self, brand, model, year,capacity):
		self.brand = brand
		self.model = model
		self.year  = year
		self.capacity  = capacity

	def toString(self):
		return "\nCAPACITY: "+str(self.capacity)+"Kgm"
