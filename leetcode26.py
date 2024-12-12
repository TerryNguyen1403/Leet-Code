def removeDuplicates(nums):
    n = len(nums)

    if n == 0 or n == 1:
        return n

    i, j = 1, 1

    while j < n:
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1

        j += 1

    return i