from random import randint as random
from time import process_time as time


arr = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)
swap = True

start = time()
while swap:
    swap = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swap = True
end = time()

print(f"{arr}\n{end}")
