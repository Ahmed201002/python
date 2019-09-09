fruit={"orange":"a sweet,orange,cirtus fruit",
       "apple":"good for making cider",
       "lemon":"a sour,yellow cirtus fruit",
       "grape":"a small,sweet fruit growing in bunches",
       "lime":"a sour ,green cirtus fruit "}
fruit["tomato"]="not good with ice "
f_tubel=tuple(fruit.items())


for snack in f_tubel :
    item,describtion=snack
    print(item+" is- "+describtion)
print(dict(f_tubel)) # we create dictionery from tuple with help of function dict

#fruit.keys()
#fruit.items()