"""
This module depicts a simple DEADLOCK example
Soldiers need both a sword and shield before they are considered fully equipped
In this code:
Soldier 1 takes a shared sword lock
Soldier 2 takes a shared shield lock
Soldier 1 now needs a shield lock, and soldier 2 needs a sword lock
Each soldier is holding a lock the other needs. This is a deadlock, where the program
can not continue because each thread holds onto a lock the other thread needs

SOLUTION:
A thread will temporarily release their lock if they can't acquire the other lock within
a specified time. This allows the other thread a chance to acquire both locks. Timing of the
lock releases is critical in this solution
"""

import threading
import time

sword_lock = threading.Lock()
shield_lock = threading.Lock()

def equip_1():
    SLEEP_TIME = 0.3 #important both threads don't have the same sleep time to increase chances of preventing deadlock
    got_both = False
    while not got_both:
        got_sword = sword_lock.acquire(timeout=1)
        if got_sword:
            print("Soldier 1 got sword, sleeping")
            time.sleep(SLEEP_TIME) #sleep after acquiring lock
            print("Soldier 1 has sword, trying to get shield")
            got_shield = shield_lock.acquire(timeout=1)
            if got_shield:
                print("Soldier 1 got shield, sleeping")
                time.sleep(SLEEP_TIME) #sleep after acquiring lock
                got_both = True
            else:
                print("Soldier 1 didn't get shield in time, releasing sword")
                sword_lock.release()
                time.sleep(SLEEP_TIME) #sleep after release to allow other thread a chance to acquire it

    print("***SUCCESS!*** Soldier 1 got both, went to battle and releasing both")
    shield_lock.release()
    sword_lock.release()

def equip_2():
    SLEEP_TIME = 0.2 #important both threads don't have the same sleep time to increase chances of preventing deadlock
    got_both = False
    while not got_both:
        got_shield = shield_lock.acquire(timeout=1)
        if got_shield:
            print("Soldier 2 got shield, sleeping")
            time.sleep(SLEEP_TIME) #sleep after acquiring lock
            print("Soldier 2 has shield, trying to get sword")
            acquired_b = sword_lock.acquire(timeout=1)
            if acquired_b:
                print("Soldier 2 got sword, sleeping")
                time.sleep(SLEEP_TIME) #sleep after acquiring lock
                got_both = True
            else:
                print("Soldier 2 didn't get sword in time, releasing shield")
                shield_lock.release() #temporarily release lock
                time.sleep(SLEEP_TIME) #sleep after release to allow other thread a chance to acquire it

    print("***SUCCESS!*** Soldier 2 got both, went to battle and releasing both")
    shield_lock.release()
    sword_lock.release()

if __name__ == "__main__":
    start = time.time()
    print("--Start threads--")

    #FIXED DEADLOCK
    soldier_thread_1 = threading.Thread(target=equip_1)
    soldier_thread_2 = threading.Thread(target=equip_2)

    soldier_thread_1.start()
    soldier_thread_2.start()

    soldier_thread_1.join()
    soldier_thread_2.join()

    print(time.time() - start)
