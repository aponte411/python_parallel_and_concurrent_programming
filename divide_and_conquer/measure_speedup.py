import time
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Optional, Any


def seq_sum(low: int, high: int) -> int:
    return sum(range(low, high))

def par_sum(
    low: int,
    high: int,
    pool: Optional[ProcessPoolExecutor] = None,
) -> Any:
    if not pool:
        with ProcessPoolExecutor() as pool:
            result = par_sum(low, high, pool)
            return sum(future.result() for future in as_completed(result))
    else:
        if high - low <= 10000:
            return [pool.submit(sum, range(low, high))]
        else:
            pivot = (high+low)//2
            left = par_sum(low, pivot, pool)
            right = par_sum(pivot, high, pool)
            return left+right

if __name__ == "__main__":
    print("Starting experiment to measure speedup and efficiency")
    NUM_EVAL_RUNS = 1
    SUM_VALUE = 1000000
    print(f"Number of evaluation runs: {NUM_EVAL_RUNS}")
    print(f"Summing up to {SUM_VALUE}")
    print("Starting sequential implementation")
    seq_result = seq_sum(1, SUM_VALUE)
    seq_time = 0
    for _ in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        res = seq_sum(1, SUM_VALUE)
        seq_time += time.perf_counter() - start
    seq_time /= NUM_EVAL_RUNS

    print("Starting parallel implementation")
    par_result = par_sum(1, SUM_VALUE)
    par_time = 0
    for _ in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        res = par_sum(1, SUM_VALUE)
        par_time += time.perf_counter() - start
    par_time /= NUM_EVAL_RUNS

    assert seq_result == par_result
    print(f"Average sequential time: {seq_time*1000} ms")
    print(f"Average parallel time: {par_time*1000} ms")
    print(f"Speedup: {seq_time/par_time}")
    print(f"Efficieny: {100*(seq_time/par_time)/mp.cpu_count()}")

