# Read & analyze the classes below.
# Then, answer the questions that follow.

class Luggage(object):
	"""docstring for Luggage"""
	def __init__(self, l, w, h):
		self.l = l
		self.w = w
		self.h = h
		self.packed = False

	def pack(self):
		if self.packed:
			print("bag is already packed")
		else:
			self.packed = True

	def unpack(self):
		if not self.packed:
			print("bag isn't packed yet")
		else:
			self.packed = False

	def dimensions(self):
		return (self.l,self.w,self.h)

class Roller(object):
	"""docstring for Roller"""
	def __init__(self, wheels):
		self.wheels = wheels
	
	def push(self):
		print("Wheeeeeee!")

	def wheelCount(self):
		return self.wheels


class Cart(Roller):
	"""docstring for Cart"""
	def __init__(self):
		Roller.__init__(self, 4)

	def push(self):
		print("Screeeeeech!")

class Duffle(Luggage):
	"""docstring for Duffle"""
	def __init__(self, l, wh):
		super(Duffle, self).__init__(l, wh, wh)
		
class RollyLuggage(Luggage, Roller):
	"""docstring for RollyLuggage"""
	def __init__(self, l, w, h):
		Luggage.__init__(self, l,w,h)
		Roller.__init__(self, 2)

print("DUFFLE:")
df = Duffle(20, 5)
print(df.dimensions())
df.pack()
df.pack()
df.unpack()

print("\nCART:")
ct = Cart()
ct.push()
print(ct.wheelCount())

print("\nROLLYLUGGAGE:")
rl = RollyLuggage(5, 5, 5)
print(rl.wheelCount())
print(rl.dimensions())
rl.push()
rl.pack()
rl.unpack()
rl.unpack()

# Q1 - What would Python print?
	#DUFFLE
	#20, 5, 5
	#bag is already packed
	#
	#CART:
	#Screeeeeech!
	#4
	#
	#ROLLYLUGGAGE:
	#2
	#5,5,5
	#Wheeeeee!
	#bag isn't packed yet 

# Q2 - What is the data type of the value returned by the dimensions method?
	#integer/instance variables 

# Q3 - Name the class(es) with single inheritance.
	#Cart, Duffle

# Q4 - Name the class(es) with multiple inheritance.
	#RollyLuggage

# Q5 - Name the instance variables in the Luggage init method.
	#self.l, self.w, self.h, self.packed

# Q6 - How many Luggage objects are created?
	#2 - df & rl

# Q7 - How many Roller objects are created?
	#2 - ct & rl

# Q8 - Explain how the super method works.
	# line 50 - so it has super because it is calling the super method, which is Luggage in this case; it is then followed by the class name, 
	# and self in parentheses, followed by a dot and then the init_method because with the paramenters of the Luggage superclass's initmethod,
	# which is l, w, and h, and it's followed after a dot because these parameters will eventually become variables that are attributes for the
	# object currently being created 

# Q9 - Explain how the resolution rule would be executed in the RollyLuggage class.
	#Since the resolution ruels describes a depth-first, left-to-right format, the derived class is follwed by the base classes in respective order 

# Q10 - In line 68, why is "Screeeeeech!" printed instead of "Wheeeeeee!"?
	# Though the derived class Cart inherits attributes and behavior methods from its parent class Luggage, the attributes and features within the 
	# derived class override those in the parent class so the push method in the Cart class will take precedence over the push method in the Luggage
