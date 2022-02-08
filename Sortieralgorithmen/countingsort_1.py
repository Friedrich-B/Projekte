from random import randint as random
from time import process_time as time


arr = []
for i in range(100):
    arr.append(random(-1000, 1000))

print(arr)

start = time()
content = []
for i in range(min(arr), max(arr) + 1):
    content.append(i)

times = []
for i in content:
    x = 0
    for j in arr:
        if i == j:
            x += 1
    times.append(x)

arr = []
for i in range(len(content)):
    for j in range(times[i]):
        arr.append(content[i])
end = time()

print(f"{arr}\n{end}")
