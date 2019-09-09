# import time
# # print(time.gmtime(0))
# # print(time.localtime())
# # print(time.time())
# time_here=time.localtime()
# # print(time_here)
# # print("The Year is:",time_here.tm_year)
# # print("the Month is:",time_here.tm_mon)
# # print("The Day is :",time_here.tm_mday)
# for i in range(5):
#     print(time_here[i])
import time
#from time import time as my_timer
#### we have 3 function to calculate elapsed time
#from time import perf_counter as my_timer
#from time import monotonic as my_timer
####to calculate the time token by cpu we use process_time
from time import process_time as my_timer

import random
input("pls enter to start")
wait_time=random.randint(1,6)
time.sleep(wait_time)
start_time=my_timer()
input("please enter to stop")
end_time=my_timer()
print("Started at "+time.strftime("%X",time.localtime(start_time)))
print("Ended at "+time.strftime("%X",time.localtime(end_time)))
print("your reaction was in {} seconds".format(end_time-start_time))
