class GreetingCard(object):
	numberSold = 0
	"""docstring for GreetingCard"""
	def __init__(self, coverPic, insideMessage):
		#super().__init__()
		self.cover = coverPic
		self.inside = insideMessage
		self.unpurchased = True

	def writeMessage(self, message):
		if (self.unpurchased):
			print("You need to buy that first!")
		else:
			self.inside += "\n\n" + message

	def buyCard(self):
		self.unpurchased = False
		GreetingCard.numberSold += 1 #

	@staticmethod
	def howManySold():
		print(str(GreetingCard.numberSold) + " cards have been sold.")


storeCards = [GreetingCard("flowers","My condolences"), GreetingCard("dog", "Happy Birthday!")]

print(storeCards[0].inside)
print("************")
storeCards[0].writeMessage("Sincerely,\nArin")
print("************")
storeCards[0].buyCard() # now 1
storeCards[1].buyCard() # now 2
storeCards[0].writeMessage("Sincerely,\nDaniel")
print(storeCards[0].inside)
print("************")
GreetingCard.howManySold()

#How would this program change if you changed GreetingCard.numberSold in buyCard to self.numberSold?
# GreetingCard.numberSold would not increment or change because self.numberSold is not calling the class. self.numberSold is an instance

#What are/is the static variable(s)?
#numberSold

#What are/is the instance variable(s)?
#cover,inside,unpurchased

#What are/is the global variable(s)?
#storeCards