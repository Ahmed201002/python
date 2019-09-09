
fruit={"orange":"a sweet,orange,cirtus fruit",
       "apple":"good for making cider",
       "lemon":"a sour,yellow cirtus fruit",
       "grape":"a small,sweet fruit growing in bunches",
       "Lime":"a sour ,green cirtus fruit "}

fruit["pear"]="an odd shaped apple " #to add entry to the dictionary
#print (fruit["grape"])     == print(fruit.get("grape"))

# del fruit["grape"] #to delete something from the list
# print(fruit)
# #del fruit     #we delete hier the dictionary it is not more available
# fruit.clear()
# print(fruit)
while True:
    dict_key=input("the fruit is : ")

    if dict_key=="quit":
            break
    description=fruit.get(dict_key,"we dont have the sort"+dict_key) #other way from if and else
    print(description)

    # if dict_key in fruit:
    #     description=fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("we dont have the fruit"+dict_key)
    #
    #

