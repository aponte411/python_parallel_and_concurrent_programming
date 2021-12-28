import multiprocessing as mp
import time

serving_line = mp.Queue(5)

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


def soup_consumer():
    while True:
        bowl = serving_line.get()
        print(f"Ate {bowl}")
        cpu_work(4)
        serving_line.task_done()

if __name__ == "__main__":
    # Create more consumers/workers than producers
    for consumer in range(2):
        mp.Process(target=soup_consumer,args=(serving_line,),daemon=True).start()
    mp.Process(target=soup_producer,args=(serving_line,)).start()
    serving_line.join()

