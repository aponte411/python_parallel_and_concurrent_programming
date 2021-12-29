from concurrent.futures import ProcessPoolExecutor
import os

def vegetable_chopper(id: int):
    name = os.getpid()
    print(f"{name} chopped a vegetable {id}")

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as pool:
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)
