# print("Ahmeeada".strip("A"))
# imelde="more mayhem","Imelda May","2011",((1,"pulling the Rug"),(2,"psycho"),(3,"mayhem"),(4,"Kentisch town waltz"))
# print(imelde)
# with open("imelda3txt",'w')as inzwischen:
#     print(imelde,file=inzwischen)

with open("imelda3.txt",'r')as inZwischen:
    content=inZwischen.readline()    # it is not easy to read it back into atuple variables,therefore we need a eval function
    print(content)
    Aha=eval(content)
    print(Aha)
title,artist,year,track=content
print(title)
print(artist)
print(year)
print(track)