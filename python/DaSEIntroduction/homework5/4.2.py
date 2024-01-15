import time

def insert_sort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while (j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
start_time = time.time()
insert_sort(arr)
end_time = time.time()
print(end_time - start_time)