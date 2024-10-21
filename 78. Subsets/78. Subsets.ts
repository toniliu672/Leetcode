function subsets(nums: number[]): number[][] {
	let result: number[][] = [[]];
	for (let num of nums) {
		let currentLength = result.length;
		for (let i = 0; i < currentLength; i++) {
			let subset = result[i].slice(0);
			subset.push(num);
			result.push(subset);
		}
	}
	return result;
}
