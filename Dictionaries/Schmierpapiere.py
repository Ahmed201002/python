
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
print(exits[1]["E"])