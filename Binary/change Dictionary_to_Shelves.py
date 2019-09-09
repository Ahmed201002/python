import shelve
books=shelve.open("wooow")

books["recipies"]={"blt":["bacon","lettuce","tomato","bread"],
                "beans_on_tost":["beans","bread"],
                "scrambled_eggs":["Butter","eggs","milk"],
               "soup":["tin of soup"],
               "pasta":["pasta","cheese"]}
books["maintanance"]={"stuck":["oil"], "loose":["gaffer tape"]}

print(books["recipies"]["pasta"])

books.close()

