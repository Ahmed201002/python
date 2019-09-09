# cities=["Berlin","Hamburg","Bonn","Wolfsburg","Achen"]
#
#
# with open("cities.txt", "w")as speicherPlatz:
#
#     for zeiger in cities:
#
#         print(zeiger,file=speicherPlatz)

cities=[]
with open("cities.txt",'r')as memory:
    for ss in memory:
        cities.append(ss.strip('\n'))


print(cities)
for kalb in cities:
    print(kalb,end='')
