#Random values
import random
for i in range(3):
    print(random.random())
    

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Mitchelle', 'Bob']
leader = random.choice(members)
print(leader)

#DICE
import random
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return(first, second)


dice = Dice()
print(dice.roll())