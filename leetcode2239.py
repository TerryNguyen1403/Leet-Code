def findClosestNumber(nums):
    distance = nums[0]

    for num in nums:
        if abs(num) < abs(distance):
            distance = num

    if abs(distance) in nums:
        return abs(distance)

    return distance