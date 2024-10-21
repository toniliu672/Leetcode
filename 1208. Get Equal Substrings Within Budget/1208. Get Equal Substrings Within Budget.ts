function equalSubstring(s, t, maxCost) {
	let n = s.length;
	let maxLen = 0;
	let currentCost = 0;
	let start = 0;

	for (let end = 0; end < n; end++) {
		currentCost += Math.abs(s.charCodeAt(end) - t.charCodeAt(end));

		while (currentCost > maxCost) {
			currentCost -= Math.abs(s.charCodeAt(start) - t.charCodeAt(start));
			start++;
		}

		maxLen = Math.max(maxLen, end - start + 1);
	}

	return maxLen;
}
