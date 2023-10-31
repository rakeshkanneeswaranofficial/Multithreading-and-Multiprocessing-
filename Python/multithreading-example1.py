# Author: Rakesh Kanneeswaran Maravar
# LinkedIn: https://www.linkedin.com/in/rakeshkanneeswaran/
# GitHub: https://github.com/rakeshkanneeswaranofficial
#please read the comments at the ending  to understand the code 
#please read the comments below to understand the code 



import time
import threading
#threading is a module in python which is used to create threads in python . the thread is a small part of a process or a program or code. 

myarr = []
def calc_square(numbers):
    print("calculating square numbers")
    for num in numbers:
        time.sleep(0.2)
        print('square:', num*num)
        myarr.append(num*num)
    print("printint done")    




def calc_cube(numbers):
    print("calculating square numbers")
    for num in numbers:
        time.sleep(0.2)
        print('square:', num*num*num)
        myarr.append(num*num*num)
    print("printint done") 


arr = [2,3,8,9]
arr1 = [4,5,7,10]


t = time.time()
t1 = threading.Thread(target=calc_square, args=[arr]) #t1 is a thread object which is created by threading.Thread() method.
t2 = threading.Thread(target=calc_square, args=[arr1])#t2 is a thread object which is created by threading.Thread() method.
t1.start()
t2.start()

t1.join()
t2.join()
print("done in : ",time.time()-t)
print(myarr)



# here we are using threading module to create two threads t1 and t2. 
# but if you see the result myarr is not empty because the two threads are running in the same memory space and they can share the memory space.




