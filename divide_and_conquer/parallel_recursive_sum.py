"""
Recursive sum is CPU Bound..so to get around the GIL
we'll run this in parallel using multiple processes.
"""

from concurrent.futures import ProcessPoolExecutor, as_completed

def recursive_sum(low, high, pool = None):
    if not pool:
        with ProcessPoolExecutor() as pool:
            futures = recursive_sum(low, high, pool)
            return sum(f.result() for f in as_completed(futures))
    else:

        if high - low <= 100000:
            return [pool.submit(sum, range(low, high))]
        else:
            pivot = (high + low)//2
            left = recursive_sum(low, pivot, pool)
            right = recursive_sum(pivot, high, pool)

            return left+right


if __name__ == "__main__":
    total = recursive_sum(1, 1000000)
    print(f"The total sum is {total}")


