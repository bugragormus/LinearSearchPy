import random
import time

# Array Length
n = 10000

# Generating Random Array
arr = [random.randint(0, 1000000) for i in range(n)]

# Finding The Largest Number (Linear Search)
start_time = time.time()

max_num = arr[0]
for num in arr:
    if num > max_num:
        max_num = num

end_time = time.time()

print("*" *150)
print("Linear Search")
print("Largest Number:", max_num)
print("Time:", end_time - start_time, "Second")

print("*" *150)

# Finding The Largest Number (BruteForce)
start_time = time.time()

max_num = arr[0]
for i in range(n):
    is_max = True
    for j in range(n):
        if arr[j] > arr[i]:
            is_max = False
            break
    if is_max:
        max_num = arr[i]

end_time = time.time()

print("Brute Force")
print("Largest Number:", max_num)
print("Time:", end_time - start_time, "Second")

print("*" *150)

print("max() Method")
print("Largest Number:", max(arr))
print("*" *150)