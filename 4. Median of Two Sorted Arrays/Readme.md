### Algorithms

Ensure that nums1 is the smaller array, so we can perform binary search on it.
Initialize left and right pointers to the start and end of nums1.
While left is less than or equal to right, do the following:

Calculate the partition points partitionX and partitionY for nums1 and nums2, respectively.
Calculate the maximum values to the left of the partitions (maxLeftX and maxLeftY) and the minimum values to the right of the partitions (minRightX and minRightY).
If the maximum values to the left are less than or equal to the minimum values to the right, we have found the correct partitions.

If the combined length of the arrays is even, return the average of the maximum value of the left partitions and the minimum value of the right partitions.
If the combined length of the arrays is odd, return the maximum value of the left partitions.


If the maximum value to the left of nums1 is greater than the minimum value to the right of nums2, move the right pointer to the left.
Otherwise, move the left pointer to the right.