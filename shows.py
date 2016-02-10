#!/usr/bin/python3

# ===========================================================================
# Show List Class
# ===========================================================================

class Shows(object):

  def __init__(self):
    self.list = []
    self.list.append("The Jambulance")
    self.list.append("Bear Bacon")
  

if __name__ == '__main__':
  print("Current KTEQ Shows: ")
  s = Shows()
  for show in s.list:
    print(show)  

