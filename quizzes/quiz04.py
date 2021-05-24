# place any import statements here (if needed)

class Police():
	# declare any static variables here
	heroesAvailable = []

	def __init__(self, precinct, leader, force, city):
		# fill in instantiations 
		self.precinct = precinct
		self.leader = leader
		self.force = force
		self.city = city
		self.backup = False
		self.backuplevel = 0
		self.level = 0

	def call_backup(self, level, street):
		# Change the police status to indicate that they need back up.
		# If the back up level is greater than 5, return a string requesting a hero for back up. See assert statement.
		# Otherwise, contact headquarters using the contact_hq method & return a string "Contact headquarters."
		self.backup = True
		self.backuplevel = level
		if self.backuplevel > 5:
			return "Hero needed to protect " + self.city + " at " + street
		else:
			self.contact_hq(level)
			return "Contact headquarters."

	def contact_hq(self, level):
		# Call the dispatch_cops method
		self.dispatch_cops(level)

	def dispatch_cops(self, num):
		# Decrease the available force for this police dept by the num indicated
		self.force = self.force - num

	def return_to_hq(self, num):
		# Increase the available force for this police dept by the num indicated
		self.force = self.force + num
		
	def launch_signal(self, targetHero):
		# Call the receive_signal method from the Hero class to contact the target hero.
		Hero.receive_signal(targetHero)

	@staticmethod
	def how_many_on_call():
		# Using list comprehension, looping, or HOFs, return the number of heroes available on call
		return len(Police.heroesAvailable)

class Hero():
	# declare any static variables here

	def __init__(self, alias, identity, power, city):
		# fill in instantiations
		# When a Hero object is created, they should be added to the heroes on call for all police departments
		self.alias = alias
		self.identity = identity
		self.power = power
		self.city = city
		Police.heroesAvailable.append(self)
		self.statusAcknowledged = False
		self.saved = 0
		self.gadgetstock = {}

	def receive_signal(self):
		# Change the hero's status to indicate that they acknowledged a call for back up
		self.statusAcknowledged = True

	def save_the_day(self, civilians):
		# If the hero has acknowledged a call for back up, increase the number of civilians saved
		# and change that status to no longer acknowledging a call for backup and return a string of "Mission accomplished."
		# Otherwise, return a string to indicate that everything is calm in their city. See assert below.
		if self.statusAcknowledged == True:
			self.saved += civilians
			self.statusAcknowledged = False
			return "Mission accomplished."
		else:
			return "All appears calm in " + self.city 

	def order_gadgets(self, gadget, num):
		# Each hero should have a dictionary to track their gadgets.
		# The gadget is the key; The num is the value (i.e. how many of that gadget)
		self.gadgetstock[gadget] = num

class TeenTitan(Hero):
	# declare any static variables here
	allTeenTitans = []
	allTeenTitansHW = []

	def __init__(self, alias, identity, power, city, experience):
		# fill in instantiations
		Hero.__init__(self, alias, identity, power, city)
		self.experience = experience
		self.partner = False
		self.hwFinished = False
		TeenTitan.allTeenTitans.append(self)

	def train(self, partner):
		# A Teen Titan's experience increases by 1
		# If they train with another Teen Titan as their partner, the partner's experience is also increased by 1
		self.experience = self.experience + 1
		if self.partner == True:
			self.partner.experience = self.partner.experience + 1

	def finish_hw(self):
		# Change the Teen Titan's homework status to finished
		self.hwFinished = True

	@staticmethod
	def evening_out():
		# Only Teen Titans who finished their homework are allowed to head out for the evening.
		# Return a string which indicates which Teen Titans can be out for the evening. See assert.
		begin = "These titans will be out for the evening:"
		for i in TeenTitan.allTeenTitans:
			if i.hwFinished == True:
				begin = begin + "\n" + i.alias
		return begin

	@staticmethod
	def new_day():
		# All Teen Titans' homework statuses are switched back to unfinished since it is a new day
		for i in TeenTitan.allTeenTitans:
			i.hwFinished = False

	@staticmethod
	def titans_go():
		# Return a list of Teen Titans who have experience above 11
		for i in TeenTitan.allTeenTitans:
			if i.experience > 11:
				TeenTitan.allTeenTitansHW.append(i.alias)
		return TeenTitan.allTeenTitansHW

# Police creation
gcpd = Police("Gotham City Police Dept.", "James Gordon", 295, "Gotham City") 
nypd = Police("New York Police Dept.","James O'Neill", 34000, "New York City")

# Hero creation
b = Hero("Batman", "Bruce Wayne", None, "Gotham City")
s = Hero("Superman", "Clark Kent", "Invincibility", "Metropolis")
i = Hero("Iron Man", "Tony Stark", "Engineering", "New York City")
ca = Hero("Captain America", "Steve Rogers", "Super strength", "New York City")
r = TeenTitan("Robin", "Dick Grayson", None, "Jump City", 12)
sf = TeenTitan("Starfire", "Koriandr", "Starbolts", "Jump City", 13)
bb = TeenTitan("Beast Boy", "Garfield Logan", "Shapeshifting", "Jump City", 11)
rv = TeenTitan("Raven", "Rachel Roth", "Psionics", "Jump City", 11)
c = TeenTitan("Cyborg", "Victor Stone", "Super strength", "Jump City", 11)

# Superheroes on call
assert(Police.how_many_on_call() == 9)

# Hero needed as backup
gcpd.call_backup(7, "45th Street")
assert(gcpd.call_backup(7, "45th Street") == "Hero needed to protect Gotham City at 45th Street")
gcpd.launch_signal(b)
b.order_gadgets("batarang", 9)
b.order_gadgets("batspray", 3)
b.order_gadgets("atomic battery", 2)
assert(b.gadgetstock["batarang"] == 9)
assert(len(b.gadgetstock.keys()) == 3)
assert(b.save_the_day(27) == "Mission accomplished.")
gcpd.call_backup(7, "22nd Street")
gcpd.launch_signal(b)
b.save_the_day(10)
assert(b.saved == 37)

# Additional cops needed as backup
nypd.call_backup(5, "Broadway")
assert(nypd.force == 33995)
nypd.return_to_hq(5)
assert(nypd.force == 34000)
assert(i.save_the_day(2) == "All appears calm in New York City")

# Teen Titans training
rv.train(sf)
c.train(None)
assert(TeenTitan.titans_go() == ["Robin", "Starfire", "Raven", "Cyborg"])

# Teen Titans homework
r.finish_hw()
sf.finish_hw()
assert(r.evening_out() == "These titans will be out for the evening:\nRobin\nStarfire")
c.new_day()
assert(r.hwFinished == False)

