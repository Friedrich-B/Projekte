from random import randint as random
from time import process_time as time


arr = []
arr_n = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)

start = time()
for i in range(min(arr), max(arr) + 1):
    for j in range(len(arr)):
        if arr[j] == i:
            arr_n.append(i)
end = time()
arr = arr_n

print(f"{arr}\n{end}")
