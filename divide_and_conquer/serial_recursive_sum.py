import time

def recursive_sum(low: int, high: int) -> int:
    if high - low <= 100000:
        return sum(range(low, high))
    pivot = (high+low)//2
    left = recursive_sum(low, pivot)
    right = recursive_sum(pivot, high)
    return left+right

if __name__ == "__main__":
    start = time.time()
    total = recursive_sum(1, 1000000)
    print(f"Runtime: {time.time() - start}")
    print(f"The total sum is {total}")
