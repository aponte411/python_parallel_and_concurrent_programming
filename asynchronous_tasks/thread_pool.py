import threading
from concurrent.futures import ThreadPoolExecutor


def vegetable_chopper(id: int):
    name = threading.current_thread().getName()
    print(f"{name} chopped vegetable {id}")


if __name__ == "__main__":
    # Useful for a bunch of I/O bound tasks..the number of threads will exceed the number of processors
    pool = ThreadPoolExecutor(max_workers=5)
    for vegetable in range(100):
        pool.submit(vegetable_chopper, vegetable)
    pool.shutdown()
