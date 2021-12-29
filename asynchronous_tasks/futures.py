import time
from concurrent.futures import ThreadPoolExecutor

def how_many_vegetables():
    print("Olivia is counting veggies...")
    time.sleep(3)
    return 42

if __name__ == "__main__":
    print("Baron asks Olivia how many veggies are in the pantry")
    with ThreadPoolExecutor() as pool:
        future = pool.submit(how_many_vegetables)
        print("Baron can do other things while he waits for the result")
        print(f"Olivia responded: {future.result()}")
