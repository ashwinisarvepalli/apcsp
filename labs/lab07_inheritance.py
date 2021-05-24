# Lab 07: Classes & Inheritance
# For extra practice (optional), see CS61A lab on OOP: http://inst.eecs.berkeley.edu/~cs61a/fa17/lab/lab06/

class Book(object):
	# Add any static variables here
	suggestBooks = []

	def __init__(self, title, author, genre):
		# Add code here
		self.title = title
		self.author = author
		self.genre = genre
		self.available = True
		self.previousBorrowers = []
		Book.suggestBooks.append(self)
		self.owner = None

	def basic_info(self):
		# Return a descriptive string with the title, author, & genre. 
		# See assert for correct formatting of string
		return "Title: " + self.title + "\n" + "Author: " + self.author + "\n" + "Genre: " + self.genre

	def check_out(self, borrower):
		# Allows the book to be checked out only if someone has not already borrowed it
		# If the book is available, add the borrower's name to a list of previous borrowers for that book
		# If the book is not available, return "This is already checked out!"
		if self.available == True:
			self.previousBorrowers.append(borrower)
			self.available = False
			self.owner = borrower
			return True
		else: 
			return "This is already checked out!"
			return False

	def return_book(self):
		# Change the book's status to not checked out (i.e. available)
		self.available = True

	def prev_borrowers(self):
		# Return a descriptive string with all previous owners, each on a new line. 
		# See assert for correct formatting of string
		begin = self.title + " was checked out by:"
		for i in self.previousBorrowers:
			begin = begin + "\n" + i 
		return begin

	@staticmethod
	def suggest_book():
		# Looks through the inventory of books & suggests the first available book
		# Returns a descriptive string indicating the first book not checked out
		# See assert for correct formatting of string
		for elem in Book.suggestBooks:
			if elem.available:
				return "I suggest you check out " + elem.title

class Textbook(Book):
	# Add any static variables here
	textbooksedition = []

	def __init__(self, title, author, genre, edition, subject):
		# Include statement to indicate that Textbook inherits from Book
		# The genre for all Textbook objects is "Educational Research"
		Book.__init__(self, title, author, "Educational Research")
		self.edition = edition
		self.subject = subject
		Textbook.textbooksedition.append(self)


	def course(self):
		# Return the textbook's subject
		return self.subject

	def sell(self, newOwner):
		# A textbook can only be sold if it is checked out.
		# The owner of the textbook becomes the newOwner.
		# If a textbook is not checked out, it cannot be sold. Return "You cannot sell that!"
		if self.check_out == True:
			self.owner = newOwner
		else:
			return "You cannot sell that!"

	@staticmethod
	def update():
		# The school updates every textbook's edition. Increase each edition by 1.
		for elem in Textbook.textbooksedition:
				elem.edition += 1
		return elem.edition

class Science(Textbook):
	# All science textbooks have a master equipment dictionary.
	# Each entry contains a key-value pair.
	# Each key is the name of the tool. Each value indicates how many there are of that tool.
	equipment = {"goggles": 8}

	def __init__(self, title, author, genre, edition, subject):
		# Include statement to indicate that Science inherits from Textbook
		# The subject for all Science objects is, naturally, "Science"
		Textbook.__init__(self, title, author, genre, edition, "Science")
		self.gogglesWorn = False
		self.labList = []

	def wear_googles(self):
		self.gogglesWorn = True

	def remove_googles(self):
		self.gogglesWorn = False

	def conduct_lab(self, labTopic):
		# Before conducting a lab from the science textbook, goggles must be worn
		# If goggles are worn, add the labTopic to a list of labs covered
		# If goggles are not worn, return "Safety comes first!"
		if self.gogglesWorn == True:
			self.labList.append(labTopic)
		else:
			return "Safety comes first!"

	def need_to_replace(self):
		# If a Science textbook's edition is 4 or below, then return "Replace your book"
		# Otherwise, return "Up to date!"
		if self.edition <= 4:
			return "Replace your book"
		else:
			return "Up to date!"

	def labs_covered(self):
		# Return a descriptive string of the labs covered for that particular Science textbook.
		# See assert for correct formatting of string
		begin = "Labs covered are:"
		for i in self.labList:
			begin = begin + "\n" + i 
		return begin

	@staticmethod
	def order_equipment(tool):
		# If the tool is in the equipment dictionary, increase that key's value by 1
		# If the tool is not in the equipment dictionary, add that entry with value 1
		if tool in Science.equipment.keys():
			Science.equipment[tool] = Science.equipment[tool] + 1
		else: 
			Science.equipment[tool] = 1

	@staticmethod
	def how_many(tool):
		# If the tool is not in the dictionary, return "Equipment not found."
		# If the tool is in the dictionary, return how many there are of that tool
		if tool in Science.equipment.keys():
			return Science.equipment[tool]
		else:
			return "Equipment not found."

# Book construction
book1 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy Adventure")
book2 = Book("Harry Potter and the Goblet of Fire", "J.K. Rowling","Fantasy Adventure")
book3 = Book("Hamlet", "Shakespeare", "Tragedy")
book4 = Book("Odyssey", "Homer", "Epic Poetry")
book5 = Book("Animal Farm", "George Orwell", "Political satire")
assert(book4.basic_info() == ("Title: Odyssey" + "\n" + "Author: Homer" + "\n" + "Genre: Epic Poetry"))

# Checking out & returning books
book2.check_out("Padma Patil")
assert(book2.check_out("Cho Chang") == "This is already checked out!")
book2.return_book()
book2.check_out("Hermione Granger")
book2.return_book()
book2.check_out("Parvati Patil")

assert(book2.prev_borrowers() == "Harry Potter and the Goblet of Fire was checked out by:\nPadma Patil\nHermione Granger\nParvati Patil")
book1.check_out("Frodo Baggins")
book5.check_out("Boxer")

# Book suggestions
assert(Book.suggest_book() == "I suggest you check out Hamlet")

# Textbooks
#self, title, author, genre, edition, subject
text1 = Textbook("Oh, California", "Beverly J. Armento", "Educational Research", 5, "History") 
text2 = Textbook("Norton Anthology of American Literature", "Robert S. Levine", "Educational Research", 6, "English")
text3 = Science("Organic Chemistry", "David R. Klein", "Educational Research", 2, "Science")
text4 = Science("Life: The Science of Biology", "David E. Sadava", "Educational Research", 5, "Science")
assert(text1.basic_info() == "Title: Oh, California\nAuthor: Beverly J. Armento\nGenre: Educational Research")

# Textbook & associated course
assert(text1.course() == "History")
assert(text3.course() == "Science")

# Book Buy-Back Program
assert(text2.sell("Walt Whitman") == 'You cannot sell that!')
text2.check_out("Walt Whitman")
text2.sell("Walt Whitman")
assert(text2.owner == 'Walt Whitman')
Textbook.update()

assert(text1.edition == 6)
assert(text3.edition == 3)				

# Perform labs from the Science textbooks
assert(text4.conduct_lab("Frog dissection") == "Safety comes first!")
text4.wear_googles()
text4.conduct_lab("Frog dissection")
text4.conduct_lab("Gel electrophoresis")
assert(text4.labList == ["Frog dissection", "Gel electrophoresis"])
text4.remove_googles()
assert(text4.gogglesWorn == False)
assert(text4.labs_covered() == "Labs covered are:\nFrog dissection\nGel electrophoresis")

# Check & update Science textbook
assert(text3.need_to_replace() == "Replace your book")
Textbook.update()
Textbook.update()
assert(text3.need_to_replace() == "Up to date!")

# Update equipment list in Science textbooks, order new equipment
text3.order_equipment("Erlenmeyer flask")
text4.order_equipment("Erlenmeyer flask")
Science.order_equipment("Erlenmeyer flask")
assert(text3.how_many("Erlenmeyer flask") == 3)
Science.order_equipment("goggles")
text3.order_equipment("beaker")
text4.order_equipment("beaker")
assert(Science.how_many("goggles") == 9)
assert(Science.equipment["beaker"] == 2)
assert(Science.how_many("crucible") == "Equipment not found.")