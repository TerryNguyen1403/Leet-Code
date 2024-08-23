def merged(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)

    mergedArray = [None] * (len1 + len2)

    index = 0
    i, j = 0, 0

    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            mergedArray[index] = nums1[i]
            i += 1
        else:
            mergedArray[index] = nums2[j]
            j += 1

        index += 1

    while i < len1:
        mergedArray[index] = nums1[i]
        i += 1
        index += 1

    while j < len2:
        mergedArray[index] = nums2[j]
        j += 1
        index += 1

    return mergedArray

def findMedian(nums1, nums2):
    merged_arr = merged(nums1, nums2)
    mid_point = len(merged_arr) // 2

    if len(merged_arr) % 2 == 0:
        return (merged_arr[mid_point] + merged_arr[mid_point - 1])/2

    return merged_arr[mid_point]
