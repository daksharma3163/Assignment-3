def count_above_average(nums):
    if not nums:
        return 0
    
    average = sum(nums) / len(nums)
    count = sum(1 for num in nums if num > average)
    
    return count 

nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Count of numbers above average:", count_above_average(nums))