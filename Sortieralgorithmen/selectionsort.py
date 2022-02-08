from random import randint as random
from time import process_time as time


arr = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)

start = time()

for i in range(len(arr)):
    x = min(arr[i:len(arr)])
    x = arr.index(x, i, len(arr))
    arr[i], arr[x] = arr[x], arr[i]

end = time()

print(f"{arr}\n{end}")
