def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1 

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 


nums = input("Enter the list: ")
nums = list(map(int,nums.split()))

target = int(input("Enter the element to find: "))
if binary_search_iterative(nums, target) != -1:
    print("Found")
else:
    print("Not Found")

if binary_search_recursive(nums, target, 0, len(nums) - 1) != -1:
    print("Found")
else:
    print("Not Found")
