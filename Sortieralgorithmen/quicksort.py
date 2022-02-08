from random import randint as random
from time import process_time as time


def quick(arr):
    if len(arr) > 1:
        p, k, g = arr[0], [], []
        for i in arr[1:]: k.append(i) if i < p else g.append(i)
        return quick(k) + [p] + quick(g)
    return arr


arr_a = []
for j in range(100):
    arr_a.append(random(-1000, 1000))


start = time()
arr_a = quick(arr_a)
end = time()

print(f"{arr_a}\n{end}")
