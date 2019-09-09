ipAdress=input("pleas enter the ip address=  ")
if ipAdress[-1]!='.':

    ipAdress+="."
numberOfSegements=1
lengthOfSegment=0
# i=""
for i in ipAdress:
    if i==".":
        print("segment number is {} contains character{}".format(numberOfSegements,lengthOfSegment))
        numberOfSegements+=1
        lengthOfSegment=0

    else:
        lengthOfSegment+=1
# if i !=".":
#     print("segment number is {} contains character {} ".format(numberOfSegements,lengthOfSegment))







