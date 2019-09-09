import shelve

with shelve.open('Selftest')as fruit:
    fruit['orange']="a sweet,orange,cirtus fruit"
    fruit['apple']="good for making cider"
    fruit['lemon']="a sour,yellow cirtus fruit"
    fruit['grape']="a small,sweet fruit growing in bunches"
    fruit['lime']="a sour,green cirtus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])



with shelve.open('Selftest')as fruit:
    fruit={"orange":"a sweet,orange,cirtus fruit",
           "apple":"good for making cider",
           "lemon":"a sour,yellow cirtus fruit",
           "grape":"a small,sweet fruit growing in bunches",
           "lime":"a sour,green cirtus fruit",
           }
    print(fruit)