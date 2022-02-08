from random import randint as random
from time import process_time as time


arr = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)

start = time()
arr_n = [arr[0]]
for i in range(1, len(arr)):
    for j in range(len(arr_n)):
        if arr[i] <= arr_n[j]:
            arr_n.insert(j, arr[i])
            break
        elif j == len(arr_n)-1:
            arr_n.append(arr[i])
end = time()

print(f"{arr_n}\n{end}")
