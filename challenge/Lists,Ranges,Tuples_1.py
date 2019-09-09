menu=[]
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam"])
menu.append(["egg","bacon","spam"])
menu.append(["egg","bacon","sausage","spam"])
# print(menu)
for meal in menu:
    if not "spam"in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)

