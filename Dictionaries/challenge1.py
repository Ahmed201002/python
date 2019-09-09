
locations={0:"You are sitting in front of a computer learning python",
           1:"you are standing at the end of a road, before small brick building ",
           2:"You are at the top of hill",
           3:"You are inside the building,awell house for a small stream",
           4:"You are in avalley beside stream",
           5:"You are in the forest"}
exits={0:{"Q":0},
       1:{"W":2,"E":3,"N":5,"S":4,"Q":0},
      2: {"N":5,"Q":0},
       3:{"W":1,"Q":0},
       4:{"N":1,"W":2,"Q":0},
       5:{"W":2,"S":1,"Q":0}}
for i in exits[1].keys():
    print(i)
