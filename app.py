from ast import While
import random
names = ["Tawanda","Tanya","Anesu","Precell","Kunaka"]


class shufle:
    def __init__(self, names):
        self.names = names
        self.history = []
        # to figure out what happens when the history list have every pair possible
    

    def get_randomPerson(self):
      pair_found = False
      while pair_found == False:
       pair =  self.names[random.randrange(0, len(self.names))], self.names[random.randrange(0, len(self.names))]
       if pair[0] == pair[1]:
           continue
       if pair not in self.history:
           self.history.append(pair)
           return pair
      


pairs = shufle(names)
pairs.get_randomPerson()



   



