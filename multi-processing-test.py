import time
import concurrent.futures

start = time.perf_counter()


def new_func():
    for _ in range(100_000_000):
        count = 0
        count += 1
    return print("Finished Processing")


[new_func() for _ in range(5)]


time1 = time.perf_counter()
normal_time = time1 - start
print(f"the normal time is: {normal_time}")

with concurrent.futures.ProcessPoolExecutor() as executor:
    [executor.submit(new_func) for _ in range(5)]

time2 = time.perf_counter()
multi_time = time2-time1
print(f"the multi-time is {multi_time}")
