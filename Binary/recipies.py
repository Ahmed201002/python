import shelve
blt=["bacon","leuttuce","tomato","bread"]
beans_on_toast=["beans","bread"]
scrambled_eggs=["eggs","butter"]
soup=["tin of soup"]
pasta=["pasta","cheese"]



with shelve.open('recipes',writeback=True)as recipies:
    # recipies["blt"]=["bacon","leuttuce","tomato","bread"]
    # recipies["beans on toast"]=beans_on_toast
    # recipies["scrambled_eggs"]= scrambled_eggs
    # recipies["pasta"]=pasta
    # recipies["soup"]=soup
    # recipies["blt"].append("Butter")
    # recipies["pasta"].append("tomato")
##______________________________________________
            ####we can add items to the lists in shelves with this method#####
    # temorary_list=recipies["blt"]
    # temorary_list.append("butter")
    # recipies["blt"]=temorary_list
    #
    # temorary_list=recipies["pasta"]
    # temorary_list.append("tomato")
    # recipies["pasta"]=temorary_list

##____________________________________________________________________
    ####i can us append but i have to use writeback at the line 7

    recipies["soup"].append=("zafraan")

    for snack in recipies:
        print(snack,recipies[snack])



