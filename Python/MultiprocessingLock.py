import multiprocessing
import time

def increment(value, lock):
    for a in range(1,100):
        time.sleep(0.02)
        lock.acquire()
        value.value = value.value + 1
        lock.release()


def decrement(value, lock):
    for a in range(1,100):
        time.sleep(0.02)
        lock.acquire()
        
        value.value = value.value - 1
        lock.release()


if __name__ == "__main__":
    Value = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=increment,args=(Value,lock))
    p2 = multiprocessing.Process(target=decrement,args=(Value,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(Value.value)