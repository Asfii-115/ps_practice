def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1
    return arr


print(reverse_list([1, 2, 3, 4, 5]))


def remove_duplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


print(remove_duplicates([1, 1, 2]))


def merge_sorted(nums1, nums2):
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        if nums1[i] > nums2[j]:
            nums1[i] = nums2[j]
            j += 1
    return nums1


print(merge_sorted([1, 5, 6], [1, 2, 4]))
