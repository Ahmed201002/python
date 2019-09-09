import shelve

#with shelve.open('Selftest')as fruit:

fruit=shelve.open('Selftest2')
# fruit['orange']="a sweet,orange,cirtus fruit"
# fruit['apple']="good for making cider"
# fruit['lemon']="a sour,yellow cirtus fruit"
# fruit['grape']="a small,sweet fruit growing in bunches"
# fruit['lime']="a sour,green cirtus fruit"
# fruit["lime"]="du bist so wunderbar berlin berlin "

# while True:
#
#     description=input('what is the fruit you need to use it:')
#     if description=="quit":
#         break
#     print(fruit.get(description,"we dont have "+description))
### get function in dictionary take the value of key and give u the descriptions ,and as option what should be happend
#when we give unknown key
#============================================================================
    ####second scenario
# while True:
#     key=input("give us the fruit: ")
#     if key=="quit":
#         break
#     if key in fruit:
#         description=fruit[key]
#         print(description)
#
#     else:
#         print("we dont have this"+key)


#========================================================================
#to arrange it
# the_keys=list(fruit.keys())
# the_keys.sort()
# for f in the_keys:
#     print(f+":"+" these are "+fruit[f])
#============================================================================
for v in fruit.values():
    print(v)
for f in fruit.items():
    print(f)
fruit.close()


