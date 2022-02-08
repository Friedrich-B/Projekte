from random import randint as random
from time import process_time as time


arr = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)

swap = True
i = 0

start = time()
while swap:
    swap = False
    if i % 2 == 0:
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                print(arr)
    else:
        for j in range(-1, -len(arr), -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swap = True
                print(arr)
    i += 1
end = time()

print(f"{arr}\n{end}")
