import random
import threading
import time

charger = threading.Semaphore(4)

def cellphone():
    name = threading.current_thread().getName()
    with charger:
        print(f"{name} is charging their phone")
        time.sleep(random.uniform(1,2))
    print("Done!")

if __name__ == "__main__":
    for phone in range(10):
        threading.Thread(target=cellphone).start()
