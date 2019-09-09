# Alaa=open("training1.txt")
#
# for line in Alaa:
#     if "automotive "in line.lower():
#         print(line)
#
# Alaa.close()
#1-we have to close the file to avoid the courruptance
#2- when error occurs the error would stop  the program

# with open ("training1.txt","r")as Alaa:
#     for line in Alaa:
#         if "IAV"in line.upper():
#             print(line,end='')

#in with open() as  would care to close the file automatically
#2-the error in reading file wouldnot stop the programm



                                            #Using the readline&&readlines()

# with open("family.txt","r")as kuku:
#     line=kuku.readline()
#     while line:
#         print(line,end='')
#         line=kuku.readline()

# with open("family.txt","r")as kuku:
#     lines=kuku.readlines()
# print(lines)
# for lineya in lines[::-1]:
#     print(lineya,end='')
with open("family.txt","r")as kuku:
     lines=kuku.readlines()
print(lines)
for lineya in lines[::-1]:
    print(lineya,end='')











