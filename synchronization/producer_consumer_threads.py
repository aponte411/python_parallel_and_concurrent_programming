import threading
import queue
import time

serving_line = queue.Queue(maxsize=5)

def cpu_work(work_units: int):
    x = 0
    for worker in range(work_units * 1000000):
        x += 1


def soup_producer():
    for soup in range(20):
        serving_line.put_nowait(f"Soup #{soup}")
        print(f"Served bowl {soup}. Remaining capacity: {serving_line.maxsize - serving_line.qsize()}")
        # Simulating the CPU not doing work, maybe the consumer is doing some I/O work
        time.sleep(0.2)
    # End of queue signal
    #serving_line.put_nowait("No soup for you")
    #serving_line.put_nowait("No soup for you")


def soup_consumer():
    while True:
        bowl = serving_line.get()
        # If we reach the end of the queue, break
        #if bowl == "No soup for you": break
        print(f"Ate {bowl}")
        # Simulating the CPU not doing work, maybe the consumer is doing some I/O work
        time.sleep(0.3)
        #cpu_work(4)
        serving_line.task_done()

if __name__ == "__main__":
    # Create more consumers/workers than producers
    for consumer in range(2):
        threading.Thread(target=soup_consumer,daemon=True).start()
    threading.Thread(target=soup_producer).start()
    serving_line.join()
