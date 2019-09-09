
locations={0:"You are sitting in front of a computer learning python",
            1:"you are standing at the end of a road before small brick building ",
            2:"You are at the top of hill",
            3:"You are inside the building,awell house for a small stream",
            4:"You are in avalley beside stream",
            5:"You are in the forest"}
exits=[{"Q":0},
       {"W":2,"E":3,"N":5,"S":4,"Q":0},
       {"N":5,"Q":0},
       {"W":1,"Q":0},
       {"N":1,"W":2,"Q":0},
       {"W":2,"S":1,"Q":0}]
loc =1
while True:

      # for direction in exits[loc].keys():
      #       availableExits+=direction+","
      # print(locations[loc])      are equal to availableExists=","+join(exits[loc].keys)
      availableExits=",".join(exits[loc].keys())
      availableExits+=","
      if loc==0:
            break
      direction=input("Available exists are "+availableExits).upper()
      #notice that we use function input().upper() to obtain the letters in capital
      print()

      if direction in exits[loc]:
            loc=exits[loc][direction]
      else:
            print("you cannot go in that direction ")



