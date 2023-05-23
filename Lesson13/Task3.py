def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


result_1 = choose_func(nums1, square_nums, remove_negatives)
print(result_1)
result_2 = choose_func(nums2, square_nums, remove_negatives)
print(result_2)

