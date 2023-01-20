def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start < end:
        summ = numbers[start] + numbers[end]
        if summ > target:
            end -= 1
        elif summ < target:
            start += 1
        else:
            return start + 1, end + 1


print(twoSum([2, 3, 4], 6))
