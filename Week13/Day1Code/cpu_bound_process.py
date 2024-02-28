import time
import multiprocessing
import os

COUNT = 50000000


def countdown(n):
    print("Process ID:", os.getpid())
    while n > 0:
        n -= 1

def process_individual():
    """
    This function depicts the creation and usage of a Process object.
    """
    p1 = multiprocessing.Process(target=countdown, args=(COUNT//3,))
    p2 = multiprocessing.Process(target=countdown, args=(COUNT//3,))
    p3 = multiprocessing.Process(target=countdown, args=(COUNT//3,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

class CustomProcess(multiprocessing.Process):
    """
    This class showcases how to inherit from Process to create a custom
    Process object.
    """
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self) -> None:
        """
        The run method contains the code that is executed when this
        custom Process is started.
        """
        print("Process ID:", os.getpid())
        while self.n > 0:
            self.n -= 1

def class_process():
    """
    Creates a custom process object for each core in the computer and
    executes it.
    :return:
    """
    cpu_count = multiprocessing.cpu_count()
    processes = [CustomProcess(COUNT // cpu_count) for i in range(cpu_count)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

def process_pool():
    """
    This function showcases how to use a Process Pool to map a collection
    of data to be processed.
    """
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(countdown, [COUNT//3, COUNT//3, COUNT//3]) #// will floor count/3. ie 10/3 = 3.333, 10//3 = 3

def main():
    print("CPU Count:", multiprocessing.cpu_count())

    print("\nUsing a Process Object")
    print("-"*30)
    start = time.time()
    process_individual()
    duration = time.time() - start
    print(f"Counting down to {COUNT} took {duration: .2f} seconds")

    # print("\nUsing a Process Pool")
    # print("-"*30)
    # start = time.time()
    # process_pool()
    # duration = time.time() - start
    # print(f"Counting down to {COUNT} took {duration: .2f} seconds")

    # print("\nUsing a custom process object")
    # print("-"*30)
    # start = time.time()
    # class_process() #create 8 processes using our custom_process class
    # duration = time.time() - start
    # print(f"Counting down to {COUNT} took {duration: .2f} seconds")


if __name__ == '__main__':
    main()