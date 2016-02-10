#!/usr/bin/python3

# ===========================================================================
# PSA List Class
# ===========================================================================

class PSA(object):

  def __init__(self):
    self.list = []
    self.list.append("PSA 1")
    self.list.append("PSA 2")
  

if __name__ == '__main__':
  print("Current PSAs in Rotation: ")
  p = PSA()
  for psa in p.list:
    print(psa)  
