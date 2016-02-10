#!/usr/bin/python3

# ===========================================================================
# Show List Class
# ===========================================================================

class Shows(object):

  def __init__(self):
    self.list = []
    self.list.append("Free Play/Unscripted")
    self.list.append("~~~~~*  MONDAY   *~~~~~")
    self.list.append("TBD")
    self.list.append("Esoteric Bluegrass")
    self.list.append("Chill Vibes")
    self.list.append("The Waiting Room")
    self.list.append("Monday Night Jazz Reflections")
    self.list.append("~~~~~*  TUESDAY  *~~~~~")
    self.list.append("Whatever I Want")
    self.list.append("Twisted Love/The Recovery")
    self.list.append("The Budgie Smugglers")
    self.list.append("Pop Culture Academy")
    self.list.append("Purple Sweet Potato")
    self.list.append("~~~~~* WEDNESDAY *~~~~~")
    self.list.append("Deep Wave")
    self.list.append("Ethereal Machinations")
    self.list.append("~~~~~* THURSDAY  *~~~~~")
    self.list.append("Left of The Dial")
    self.list.append("House of Funk")
    self.list.append("Sensible Radio")
    self.list.append("On The Roof w/ Rusty & Roo")
    self.list.append("The J Waylon Programme")
    self.list.append("~~~~~*  FRIDAY   *~~~~~")
    self.list.append("Bear Bacon")
    self.list.append("The Jambulance")
    self.list.append("The B-Side")
    self.list.append("Three Lost Causes")
    self.list.append("~~~~~* SATURDAY  *~~~~~")
    self.list.append("The Progressive")
    self.list.append("Janitors of the Apocalypse")
    self.list.append("The Couch of the Blooming Youths")
    self.list.append("Under the Tundra with Jason Ader")
    self.list.append("Prayers to the Transparent Kaleidoscope")
    self.list.append("~~~~~*  SUNDAY   *~~~~~")
    self.list.append("Ramblings On Music")
    self.list.append("The Sparrow")

if __name__ == '__main__':
  print("Current KTEQ Shows: ")
  s = Shows()
  for show in s.list:
    print(show)  

