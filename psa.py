#!/usr/bin/python3

# ===========================================================================
# PSA List Class
# ===========================================================================

class PSA(object):

  def __init__(self):
    self.list = []
    self.list.append("LISTEN UP MAGGOTS")
    self.list.append("DAD O'CLOCK")
    self.list.append("HEART ATTACK SONG")
  

if __name__ == '__main__':
  print("Current PSAs in Rotation: ")
  p = PSA()
  for psa in p.list:
    print(psa)  
