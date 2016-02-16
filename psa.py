#!/usr/bin/python3

# ===========================================================================
# PSA List Class
# ===========================================================================

class PSA(object):

  def __init__(self):
    self.list = []
    self.list.append("1 in 5 Kids")
    self.list.append("Adopt")
    self.list.append("Best of Show")
    self.list.append("Be Vocal")
    self.list.append("Bullying")
    self.list.append("Buzzed Driving")
    self.list.append("Chance")    
    self.list.append("Child Hunger")
    self.list.append("Commune")
    self.list.append("Funky Chicken ESP")
    self.list.append("Stuntman")


if __name__ == '__main__':
  print("Current PSAs in Rotation: ")
  p = PSA()
  for psa in p.list:
    print(psa)  
