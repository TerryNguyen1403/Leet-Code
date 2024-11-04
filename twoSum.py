
def twoSum(nums, target):
    Map = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in Map:
            return [Map[diff],i]
        Map[n] = i
    print(Map)
            
        