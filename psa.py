#!/usr/bin/python3

# ===========================================================================
# PSA List Class
# ===========================================================================

class PSA(object):

  def __init__(self):
    self.list = []
    self.list.append("Autism Awareness")
    self.list.append("Domestic Violence Prevention")
    self.list.append("Fatherhood: Kids On Dads")
    self.list.append("Underage Drinking Pool Party")    
    self.list.append("Hunger Prevention: So Much Food")
    self.list.append("Pre-Diabetes")
    self.list.append("Recycling")
    self.list.append("Sexual Assault Prevention")
    self.list.append("Stroke Awareness: Party 60")
    self.list.append("Texting And Driving")
    self.list.sort()

if __name__ == '__main__':
  print("Current PSAs in Rotation: ")
  p = PSA()
  for psa in p.list:
    print(psa)  
