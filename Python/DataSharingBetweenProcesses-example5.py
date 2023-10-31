# Author: Rakesh Kanneeswaran Maravar
# LinkedIn: https://www.linkedin.com/in/rakeshkanneeswaran/
# GitHub: https://github.com/rakeshkanneeswaranofficial
#please read the comments at the ending  to understand the code 
#in this file we will see how to share memory objects between processes using multiprocessing.qeue.

import multiprocessing

Q = multiprocessing.Queue() #here we are creating a queue object using multiprocessing.Queue() method.

arr = [2,3,8]                            
def calc_square(numbers, Q):
    for _ in numbers:
        Q.put(_ * _)                             


if __name__ == "__main__":

    p1 = multiprocessing.Process(target = calc_square, args=(arr, Q))

    p1.start()

    p1.join()
   
     # the below code is used to print the queue object. 
     # when get() method is called on the queue object it returns the first element in the queue and removes it from the queue.
    while Q.empty() is False: #this while loop is used to print all the elements in the queue.
        print(Q.get())




#the output of the above code is
# Squaring process done
# 4
# 9
# 64


# in this code i have used multiprocessing.Queue() method to create a queue object.
# the queue object is shared between the processes.
# the queue object is a FIFO data structure.


