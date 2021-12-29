import threading

NUM_THREADS = 10
bag_of_chips = 1
pencil = threading.Lock()
fist_bump = threading.Barrier(NUM_THREADS)

def cpu_work(work_units: int) -> None:
    x = 0
    for i in range(work_units*1000000):
        x += 1


def baron_shopper():
    global bag_of_chips
    cpu_work(1)
    fist_bump.wait()
    with pencil:
        bag_of_chips *= 2
        print("Baron doubled the bag of chips")


def olivia_shopper():
    global bag_of_chips
    cpu_work(1)
    with pencil:
        bag_of_chips += 3
        print("Olivia added 3 bags of chips")
    fist_bump.wait()


if __name__ == "__main__":
    threads = []
    # We divide the total number of threads across 2 shoppers
    for i in range(NUM_THREADS//2):
        threads.append(threading.Thread(target=baron_shopper))
        threads.append(threading.Thread(target=olivia_shopper))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print(f"The final number of chips is {bag_of_chips}")
