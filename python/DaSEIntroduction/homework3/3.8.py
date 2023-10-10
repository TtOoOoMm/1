import random
import time

def generate_random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 将列表分为两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归对两个子列表进行排序
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 合并两个有序的子列表
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    
    # 比较左右两个列表的元素，将较小的放入合并列表中
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # 将剩余的元素加入合并列表
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# 生成不同长度数列
lengths = [100, 1000, 2000, 10000, 20000]
num_trials = 10

for length in lengths:
    total_time_bubble = 0
    total_time_selection = 0
    total_time_merge = 0
    total_time_quick = 0
    for _ in range(num_trials):
        random_list = generate_random_list(length)

        arr = random_list.copy()
        total_time_selection += measure_time(selection_sort, arr)

        arr = random_list.copy()
        total_time_merge += measure_time(merge_sort, arr)


    average_time_selection = total_time_selection / num_trials
    average_time_merge = total_time_merge / num_trials

    print(f"对长度为 {length} 的数列进行排序的平均时间：")
    print(f"Selection Sort: {average_time_selection:.6f} 秒")
    print(f"Insertion Sort: {average_time_merge:.6f} 秒")
    print()

