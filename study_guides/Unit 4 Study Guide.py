class Pokemon (object):
	allPKMN = []

	def __init__(self, pokeName, number, health, attackName, attackPoints, type):
		self.name = pokeName
		self.number = number
		self.original = health
		self.health = health
		self.attackName = attackName
		self.attackPoints = attackPoints
		self.type = type
		self.attackdiciton = {attackName : attackPoints}
		Pokemon.allPKMN.append(self)


	def format_number (self):
		if self.number <= 9:
			return '00' + str(self.number)
		elif self.number <= 99:
			return '0' + str(self.number)
		else:
			return str(self.number)

	def learn_attack(self, newAttack, newPoints):
		self.attackdiciton[newAttack] = newPoints
		if len(self.attackdiciton.keys()) > 4:
			x = min(self.attackdiciton.values())
			for attack, points in self.attackdiciton.items():
    				if points == x:
        				del self.attackdiciton[attack]
        	return self.attackdiciton


   	def attack(self, opponent):
   		x = max(self.attackdiciton.values())
   		opponent.health = opponent.health - x
   		if opponent.health < 0:
   			return 0
   		return opponent.health

   	def use_potion (self):
   		if self.health == 0:
   			return 'Pokemon knocked out. Go to Pokemon Center.'
   		elif self.health == self.original:
   			return 'Pokemon fully healed.'
   		else:
   			self.health += 20
   			return 'Pokemon health: ' + str(self.health)

   	@staticmethod
   	def go_to_pokecenter():
   		for i in Pokemon.allPKMN:
   			i.health = i.original
   		return str(len(Pokemon.allPKMN)) + ' Pokemon have been fully healed.'


s = Pokemon("Squirtle", 7, 50, "Bubble Beam", 10, "Water")
b = Pokemon("Bulbasaur", 1, 40, "Vine Whip", 10, "Grass")
j = Pokemon("Jigglypuff", 39, 50, "Sing", 10, "Fairy")
p = Pokemon("Pikachu", 25, 40, "Thundershock", 20, "Electric")
c = Pokemon("Charmander", 4, 50, "Flame Tail", 20, "Fire")
m = Pokemon("Mew", 151, 70, "Pay Bolt", 30, "Psychich")
g = Pokemon("Gastly", 92, 30, "Night Shade", 20, "Ghost")

# assert format number
assert(b.format_number() == '001')
assert(j.format_number() == '039')
assert(m.format_number() == '151')

#Assert for learn attack

assert(s.learn_attack("Water Gun", 30)== {'Bubble Beam' : 10, 'Water Gun' : 30})
assert(s.learn_attack("Surf", 40)==  {'Bubble Beam' : 10, 'Surf' : 40, 'Water Gun' : 30})
assert(s.learn_attack("Withdraw", 0)==  {'Bubble Beam' : 10, 'Surf' :40, 'Water Gun' : 30, 'Withdraw' : 0})
assert(s.learn_attack("Shell Attack", 25)==  {'Bubble Beam' : 10, 'Surf' :40, 'Water Gun' : 30, 'Shell Attack' : 25})

#check for attack
print(g.attack(b))
print(p.attack(b))
print(m.attack(s))

#check for use potion
print (g.use_potion()) 
print (b.use_potion())
print (s.use_potion())

#check for go to pokecenter
print(Pokemon.go_to_pokecenter())
