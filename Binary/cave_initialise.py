import shelve
locations= shelve.open("locations")

locations["0"]={"desc":"you are setting in front of computer learning python",
              "exits":{},
              "namedExits":{}}
locations["1"]={"desc":"",
              "exits":{"w":'2',"E":'3',"N":'5',"S":'4',"Q":'0'},
              "namedExits":{"2":'2',"3":'3',"5":'5',"4":'4'}}
locations["2"]={"desc":"You are at the top of hill",
              "exits":{"N":'5',"Q":'0'},
              "namedExits":{"5":'5'}}

locations["3"]={"desc":"You are inside the building,well house for a small stream",
              "exits":{"N":'1',"w":'2',"Q":'0'},
              "namedExits":{"1":'1'}},
locations["4"]={"desc":"You are in the valley beside astream",
              "exits":{"N":'1',"w":'2',"Q":'0'},
              "namedExits":{"1":'1',"2":'2'}},
locations["5"]={"desc":"You are in the forest",
              "exits":{"S":'1',"w":'2',"Q":'0'},
              "namedExits":{"1":'1',"2":'2'}}
locations.close()
vocabulary=shelve.open("vocabulary")



vocabulary["QUIT"]="Q"
vocabulary["NORTH"] = "N"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["SOUTH"] = "S"
vocabulary["WEST"] = "W"
vocabulary["ROAD"] = "1"
vocabulary["HIL"] = "2"
vocabulary["BUILDING"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"

vocabulary.close()