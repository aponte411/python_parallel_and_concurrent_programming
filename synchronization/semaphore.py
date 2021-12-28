import random
import threading
import time

# If the size of the resource is bounded, use a BoundedSemaphore()
charger = threading.Semaphore(4)

def cellphone():
    name = threading.current_thread().getName()
    with charger:
        print(f"{name} is charging their phone")
        # Some I/O bound work like connect to db and querying it
        # conn = connectdb()
        # try:
        #   use conn
        # finally:
        #   conn.close()
        time.sleep(random.uniform(1,2))
    print("Done!")


if __name__ == "__main__":
    for phone in range(10):
        threading.Thread(target=cellphone).start()
