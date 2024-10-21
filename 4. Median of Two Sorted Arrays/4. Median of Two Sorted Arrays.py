class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)
        left = 0
        right = n1

        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (n1 + n2 + 1) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float('-infinity')
            minRightX = nums1[partitionX] if partitionX != n1 else float('infinity')

            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float('-infinity')
            minRightY = nums2[partitionY] if partitionY != n2 else float('infinity')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (n1 + n2) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1