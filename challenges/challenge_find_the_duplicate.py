def find_duplicate(nums: list[int]):
    if not nums or not isinstance(nums, list) or len(nums) <= 1:
        return False
    nums.sort()
    for index, num in enumerate(nums):
        if not isinstance(num, int) or num < 0:
            return False
        if index <= len(nums) - 2 and num == nums[index + 1]:
            return num
    return False


nums = [1, 1]
print(find_duplicate(nums))
