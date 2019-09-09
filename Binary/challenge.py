locations={0:{"desc":"you are setting in front of computer learning python",
              "exits":{},
              "namedExits":{}},
           1:{"desc":"",
              "exits":{"w":2,"E":3,"N":5,"S":4,"Q":0},
              "namedExits":{"2":2,"3":3,"5":5,"4":4}},
           2:{"desc":"You are at the top of hill",
              "exits":{"N":5,"Q":0},
              "namedExits":{"5":5}},

            3:{"desc":"You are inside the building,well house for a small stream",
               "exits":{"N":1,"w":2,"Q":0},
               "namedExits":{"1":1}},
           4:{"desc":"You are in the valley beside astream",
              "exits":{"N":1,"w":2,"Q":0},
              "namedExits":{"1":1,"2":2}},
           5:{"desc":"You are in the forest",
              "exits":{"S":1,"w":2,"Q":0},
              "namedExits":{"1":1,"2":2}},}
vocabulary={"QUIT":"Q",
            "NORTH":"N",
            "SOUTH":"S",
            "EAST":"E",
            "WEST":"W",
            "ROAD":"1",
            "HILL":"2",
            "BUILDING":"3",
            "VALLEY":"4",
            "FOREST":"5" }

loc=1
while True:
    availableExits=",".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])
    if loc==0:
        break
    else:
        allExits=locations[loc]["exits"]
        allExits.update(locations[loc]["namedExits"])
        direction=input("Available exits are"+availableExits).upper()
        #parse the user input,using our vocabulary dictionary if necessary
        if len(direction)>1: #more than 1 letter,so check vocab
            words=direction.split()
            for word in words:
                if word in vocabulary:
                    direction=vocabulary[word]
                    break
        if direction in allExits:
            loc=allExits[direction]
        else:
            print("we cannot go in that direction")




