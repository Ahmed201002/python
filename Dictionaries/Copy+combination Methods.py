fruit={"orange":"a sweet,orange,cirtus fruit",
      "apple":"good for making cider",
      "lemon":"a sour,yellow cirtus fruit",
      "grape":"a small,sweet fruit growing in bunches",
      "Lime":"a sour ,green cirtus fruit "}

veg={"cabbage":"every child's favourite",
     "sprouts":"mmmm,lovely",
     "Spinash":"can i have some fruits ,please "}

#update dont return any value !
# print(veg.update(fruit))
# print(veg)
# print(fruit.update(veg))
# print(fruit)
nice_nasty=fruit.copy()
nice_nasty.update(veg)
print(nice_nasty)