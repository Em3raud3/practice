import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping... {seconds} second(s)..."


if __name__ == "__main__":
    secs = [5, 4, 3, 2, 1]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # ? results = [executor.submit(do_something, sec) for sec in secs]
        # ! (map) returns the results in the order that they were started

        results = executor.map(do_something, secs)

        for result in results:
            print(result)
# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1.5])
#     p.start()
#     processes.append(p)
# for process in processes:
#     process.join()
finish = time.perf_counter()


print(f"Finished in {round(finish-start,2)} second(s)")
