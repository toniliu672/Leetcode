function longestSubarray(nums: number[]): number {
	const n = nums.length;
	let left = 0,
		right = 0;
	let zeroCount = 0;
	let maxLen = 0;

	while (right < n) {
		if (nums[right] === 0) {
			zeroCount++;
		}

		while (zeroCount > 1) {
			if (nums[left] === 0) {
				zeroCount--;
			}
			left++;
		}

		maxLen = Math.max(maxLen, right - left);
		right++;
	}

	return maxLen;
}
