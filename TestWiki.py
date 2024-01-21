
import threading as thread
import concurrent.futures

def printTest(a, b, c, d):
    print("Test called")
    return a + b + c + d

pool = concurrent.futures.ThreadPoolExecutor(max_workers=3)
#pool.shutdown(wait=True)

total = 0

for l in range(3):
    future_object = pool.submit(printTest, 1, 2, 1, 2)
    total += future_object.result()
    
print(total)