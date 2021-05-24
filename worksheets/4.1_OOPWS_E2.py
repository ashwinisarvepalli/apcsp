class Musician(object):
	allMusicians = []
	"""docstring for Musician"""
	def __init__(self, name, age, firstComposition):
		self.name = name
		self.age = age
		self.allcompositions = [firstComposition]
		Musician.allMusicians.append(self)

	#adds the name of the composition to the musician's list of compositions
	def newComposition(self, composition):
		self.allcompositions.append(composition)
		

	#returns a string naming the artist and each composition on a new line. See the Assert statement below for an example
	def listCompositions(self):
		begin = self.name + " composed:" + "\n"
		for i in self.allcompositions:
			begin = begin + i + "\n"
		return begin

	#returns the age of the musician
	def musicianAge(self):
		return self.age

	#increases each musician's age by 1
	@staticmethod
	def yearPasses():
		for i in Musician.allMusicians:
			i.age += 1 


mozzie = Musician("Mozart", 8, "Symphony No. 1")
sally = Musician("Salieri", 20,  "Le donne letterate")
assert(mozzie.musicianAge() == 8)
assert(mozzie.listCompositions() == "Mozart composed:\nSymphony No. 1\n")
mozzie.newComposition("Symphony No. 41")
assert(mozzie.listCompositions() == "Mozart composed:\nSymphony No. 1\nSymphony No. 41\n")

print (mozzie.listCompositions())

Musician.yearPasses()
print(mozzie.musicianAge())
assert(mozzie.musicianAge() == 9)
Musician.yearPasses()
assert(sally.musicianAge() == 22)