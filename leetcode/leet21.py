def merge(nums1, nums2, m, n):
    m = m - 1
    n = n - 1
    k = m + n - 1

    i, j = 0, 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            nums1[i] = nums1[i]
            i += 1
        else:
            nums1[i] = nums2[j]
            j += 1

    return nums1


print(merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 2))
