function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
	if (nums1.length > nums2.length) {
		[nums1, nums2] = [nums2, nums1];
	}

	const n1 = nums1.length;
	const n2 = nums2.length;
	let left = 0;
	let right = n1;

	while (left <= right) {
		const partitionX = Math.floor((left + right) / 2);
		const partitionY = Math.floor((n1 + n2 + 1) / 2) - partitionX;

		const maxLeftX = partitionX === 0 ? -Infinity : nums1[partitionX - 1];
		const minRightX = partitionX === n1 ? Infinity : nums1[partitionX];

		const maxLeftY = partitionY === 0 ? -Infinity : nums2[partitionY - 1];
		const minRightY = partitionY === n2 ? Infinity : nums2[partitionY];

		if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
			if ((n1 + n2) % 2 === 0) {
				return (
					(Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2
				);
			} else {
				return Math.max(maxLeftX, maxLeftY);
			}
		} else if (maxLeftX > minRightY) {
			right = partitionX - 1;
		} else {
			left = partitionX + 1;
		}
	}

	return 0;
}
