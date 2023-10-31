# Author: Rakesh Kanneeswaran Maravar
# LinkedIn: https://www.linkedin.com/in/rakeshkanneeswaran/
# GitHub: https://github.com/rakeshkanneeswaranofficial

#please read the comments at the ending  to understand the code 


import multiprocessing

result = multiprocessing.Array('i',3) #here we are creating a shared memory object using multiprocessing.Array() method.
                                      #this is stored in different memory space and can be shared between the processes.

value = multiprocessing.Value('d',0.0) #here we are creating a shared memory object using multiprocessing.Value() method.
                                       #the first argument 'd' is the type of the value. here 'd' stands for double.
                                      
arr = [2,3,8]                            
def calc_square(numbers, result):
    value.value = 5.5
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
    print(value.value) #here we are printing the value which is a shared memory object.




#the output of the above code is
# Squaring process done
#[4, 9, 64]
#5.5


#in the code above we can see that we are using multiprocessing.Value() method to create a shared memory object.
# and adding a value to it and printing it.
