with open("Family.txt",'a')as table:
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2}".format(i,j,i*j),file=table)
        print("-"*20,file=table)


