# farm_Animal={"sheep","hen","cow"} # the first way to create a set
#
# for animal in farm_Animal:
#     print(animal)
# print("*"*40)
# Wild_animal=set(["lion","tiger","elephant","hare"])    # the second way to create a set
# Wild_animal.add("horse")
# farm_Animal.add("horse")
# print(farm_Animal)
# print(Wild_animal)
# empty_set=set()
# #empty_set1={}  #why i suppose it an empty dictionary and in dictionary we dont have add fucnction as Set.
#
# even=set(range(0,40,2))
# print("the even number is {}".format(even))
# print(len(even))
# squares_tuple=(4,6,9,16,25)
#
# squares=set(squares_tuple)
# print("the squares is {}".format(squares))
# print(len(squares))
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
# print("-"*80)
# print(even.intersection(squares)) # the intersection way 1
# print(even&squares)  # the intersection way 2

even=set(range(0,40,2))
print(sorted(even))
squares_tuples=(4,6,9,16,25)
squares=set(squares_tuples)
print(sorted(squares))
print("*"*200)
print("even minus squares")
print(sorted(even-squares))
print(sorted(even.difference(squares)))
print("squares minus evens")
print(sorted(squares-even))
print(sorted(squares.difference(even)))
