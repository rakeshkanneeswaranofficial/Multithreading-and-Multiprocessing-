# Author: Rakesh Kanneeswaran Maravar
# LinkedIn: https://www.linkedin.com/in/rakeshkanneeswaran/
# GitHub: https://github.com/rakeshkanneeswaranofficial
#please read the comments at the ending  to understand the code 
import multiprocessing #multiprocessing is a module in python which is used to create processes in python . the process is a small part of a program or code.
import time



myarrS = [] #this is a list which is used to store the square of the numbers
myarrC = [] #this is a list which is used to store the cube of the numbers

def square(numbers):
    for _ in numbers:
        time.sleep(0.2)
        print('square:', _*_)
        myarrS.append(_*_) #here we are appending the square of the number to the myarr list
    print("inside the funtion: "  + str(myarrS) )    

def cube(numbers):
    for _ in numbers:
        time.sleep(0.1)
        print('cube:', _*_*_)
        myarrC.append(_*_*_) #here we are appending the cube of the number to the myarr list
    print("inside the funtion: "  + str(myarrC) )        

  
if __name__ == "__main__": #this ensures that this code is executed only when this file is executed directly and not when it is imported in another file.
 arr = [1,2,3,4,5]
 p1 = multiprocessing.Process(target=square, args=(arr,)) #p1 is a process object which is created by multiprocessing.Process() method.
 p2 = multiprocessing.Process(target=cube, args=(arr,))#p2 is a process object which is created by multiprocessing.Process() method.
 p1.start()
 p2.start()
 p1.join()
 p2.join()

 print("result:",myarrS)
print("result:",myarrC)

 # here we are using multiprocessing module to create two processes p1 and p2. but if you see the result myarr is empty. 
 # this is because the two processes are running in their own memory space and they cannot share the memory space.
 # so if you want to share the memory space between the processes then you have to use shared memory objects.
 # this is shown in next file example 3

