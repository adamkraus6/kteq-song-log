#!/usr/bin/python3

import datetime

# ===========================================================================
# Show list Class
# ===========================================================================

MONDAY    = 0
TUESDAY   = 1
WEDNESDAY = 2
THURSDAY  = 3
FRIDAY    = 4
SATURDAY  = 5
SUNDAY    = 6

class Shows(object):

  def __init__(self):
    self.mon  = []
    self.tue  = []
    self.wed  = []
    self.thu  = []
    self.fri  = []
    self.sat  = []
    self.sun  = []
    self.list = []
    self.schedule = []

    self.mon.append("Free Play/Unscripted")
    self.tue.append("Free Play/Unscripted")
    self.wed.append("Free Play/Unscripted")
    self.thu.append("Free Play/Unscripted")
    self.fri.append("Free Play/Unscripted")
    self.sat.append("Free Play/Unscripted")
    self.sun.append("Free Play/Unscripted")

    #self.list.append("~~~~~*  SUNDAY   *~~~~~")
    self.sun.append("White Noise")
    self.sun.append("Wild Woman Radio")
    self.sun.append("Bro Jam")
    self.sun.append("The Rough Draft")
    self.sun.append("The Sparrow")
    #self.list.append("~~~~~*  MONDAY   *~~~~~")
    self.mon.append("Esoteric Bluegrass")
    self.mon.append("Chill Vibes")
    self.mon.append("The Throwback Zone")
    self.mon.append("Monday Night Jazz Reflections")
    #self.list.append("~~~~~*  TUESDAY  *~~~~~")
    self.tue.append("Twisted Love")
    self.tue.append("The Budgie Smugglers")
    self.tue.append("Pop Culture Academy")
    #self.list.append("~~~~~* WEDNESDAY *~~~~~")
    self.wed.append("The Jambulance")
    self.wed.append("Purple Sweet Potato")
    self.wed.append("The Recovery")
    #self.list.append("~~~~~* THURSDAY  *~~~~~")
    self.thu.append("Left of The Dial")
    self.thu.append("House of Funk")
    self.thu.append("CCCurtain Ratsss")
    self.thu.append("House Blend")
    #self.list.append("~~~~~*  FRIDAY   *~~~~~")
    self.fri.append("Ckaos")
    self.fri.append("Bear Bacon")
    self.fri.append("Skeletons In The Closet")
    self.fri.append("The B-Side")
    self.fri.append("Three Lost Causes")
    #self.list.append("~~~~~* SATURDAY  *~~~~~")
    self.sat.append("Janitors of the Apocalypse")        
    self.sat.append("Houston, We Have A Problem")
    self.sat.append("Under the Tundra with Jason Ader")
    self.sat.append("Prayers to the Transparent Kaleidoscope")

    self.schedule.append(self.mon)
    self.schedule.append(self.tue)
    self.schedule.append(self.wed)
    self.schedule.append(self.thu)
    self.schedule.append(self.fri)
    self.schedule.append(self.sat)
    self.schedule.append(self.sun)

    self.dayOfWeek()

  def dayOfWeek(self):
  	#clear list
    self.list[:] = []
    day = datetime.datetime.today().weekday()
    if( day == MONDAY ):
      self.list.append(self.mon)
    elif( day == TUESDAY ):
      self.list.append(self.tue)
    elif( day == WEDNESDAY ):
      self.list.append(self.wed)
    elif( day == THURSDAY ):
      self.list.append(self.thu)
    elif( day == FRIDAY ):
      self.list.append(self.fri)
    elif( day == SATURDAY ):
      self.list.append(self.sat)
    elif( day == SUNDAY ):
      self.list.append(self.sun)

    #Collapse list
    self.list = [item for sublist in self.list for item in sublist]
  
  def printFullSchedule(self):
    print("Current KTEQ Shows: ")
    for day in self.schedule:
      for show in day:
        print(show)

  def printlistsSchedule(self):
    print("Today's Schedule: ")
    self.dayOfWeek()
    for show in self.list:
      print(show)

if __name__ == '__main__':
  s = Shows()
  s.printFullSchedule()
  print("")
  s.printlistsSchedule()  

