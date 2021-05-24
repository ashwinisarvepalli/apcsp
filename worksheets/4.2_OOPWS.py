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


# Q2 - What is the data type of the value returned by the dimensions method?


# Q3 - Name the class(es) with single inheritance.


# Q4 - Name the class(es) with multiple inheritance.


# Q5 - Name the instance variables in the Luggage init method.


# Q6 - How many Luggage objects are created?


# Q7 - How many Roller objects are created?


# Q8 - Explain how the super method works.


# Q9 - Explain how the resolution rule would be executed in the RollyLuggage class.


# Q10 - In line 68, why is "Screeeeeech!" printed instead of "Wheeeeeee!"?

