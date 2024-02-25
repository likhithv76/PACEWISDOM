import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l , target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    if high < low:
        return -1
    mid = (low + high) //2
    if l[mid] == target:
        return mid
    elif target < l[mid]:
        return binary_search(l, target, low, mid-1)
    else:
        return binary_search(l , target, mid+1, high)

if __name__ == '__main__':
    user_input = input("Enter a list of numbers separated by spaces: ")
    user_list = list(map(int, user_input.split()))

    target = int(input("Enter the number to search for: "))

    print("User's list:", user_list)
    print("Target:", target)

    start = time.perf_counter()
    naive_result = naive_search(user_list, target)
    end = time.perf_counter()
    naive_time = end - start

    start = time.perf_counter()
    binary_result = binary_search(user_list, target)
    end = time.perf_counter()
    binary_time = end - start

    print("Naive search result:", naive_result)
    print("Binary search result:", binary_result)

    if naive_result != -1:
        print("Naive search found the target at index:", naive_result)
    else:
        print("Naive search did not find the target.")

    if binary_result != -1:
        print("Binary search found the target at index:", binary_result)
    else:
        print("Binary search did not find the target.")

    print("Naive search time:", naive_time, "seconds.")
    print("Binary search time:", binary_time, "seconds.")