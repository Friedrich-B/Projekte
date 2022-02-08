from random import randint as random
from time import process_time as time


arr = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)

start = time()
for h in range(len(arr)-1):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
end = time()

print(f"{arr}\n{end}")
