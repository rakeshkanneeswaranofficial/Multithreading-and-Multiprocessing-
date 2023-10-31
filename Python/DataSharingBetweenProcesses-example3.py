# Author: Rakesh Kanneeswaran Maravar
# LinkedIn: https://www.linkedin.com/in/rakeshkanneeswaran/
# GitHub: https://github.com/rakeshkanneeswaranofficial
#please read the comments at the ending  o understand the code 


import multiprocessing

result = multiprocessing.Array('i',3) #here we are creating a shared memory object using multiprocessing.Array() method.
                                      #this is stored in different memory space and can be shared between the processes.
                                      #the first argument 'i' is the type of the array. here 'i' stands for integer.
                                      #the second argument is the size of the array.

arr = [2,3,8]                            
def calc_square(numbers, result):
    for index , element in enumerate(numbers):
        result[index] = element * element
    print("Squaring process done")                                  

def calc_cube(numbers):
    for index , element in enumerate(numbers):
        result[index] = element * element * element
    print("Cubing process done")    

if __name__ == "__main__":

    p1 = multiprocessing.Process(target = calc_square, args=(arr, result))
    #p2 = multiprocessing.Process(target = calc_cube, args=(arr,))

    p1.start()
    #p2.start()

    p1.join()
    #p2.join()

    print(result[:]) #here we are printing the result which is a shared memory object.




#the output of the above code is
# Squaring process done
#[4, 9, 64]


# here we can see that the result is not empty because the result is a shared memory object and it is shared between the processes.
# this is done using multiprocessing.Array() method.
# we will see now how to use shared memory objects using multiprocessing.Value() method.
# this is shown in next file example 4
