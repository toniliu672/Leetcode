function countTriplets(arr) {
	const n = arr.length;
	const prefix_xor = new Array(n + 1).fill(0);
	for (let i = 0; i < n; i++) {
		prefix_xor[i + 1] = prefix_xor[i] ^ arr[i];
	}

	let count = 0;
	for (let i = 0; i < n - 1; i++) {
		const c = arr[i];
		for (let k = i + 1; k < n; k++) {
			const a = prefix_xor[k] ^ prefix_xor[i];
			if (a === arr[k]) {
				const b = prefix_xor[k + 1] ^ prefix_xor[k];
				if (a === b) {
					count += k - i;
				}
			}
		}
	}

	return count;
}
