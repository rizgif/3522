"""
This module depicts how to create a custom thread by inheriting from
the Thread class.
"""
import threading
import time

class MyThreadClass(threading.Thread):
    def __init__(self, io_time):
        super().__init__()
        self.io_time = io_time

    def run(self):
        time.sleep(self.io_time)

start_time = time.time()
threads = [MyThreadClass(1) for _ in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
duration = time.time() - start_time
print(f"Duration in {duration} seconds")
