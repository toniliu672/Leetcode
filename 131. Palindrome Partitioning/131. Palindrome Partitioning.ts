function partition(s) {
	let res = [];
	dfs(s, [], res);
	return res;
}

function dfs(s, path, res) {
	if (!s) {
		res.push(path);
		return;
	}
	for (let i = 1; i <= s.length; i++) {
		let sub = s.slice(0, i);
		if (isPalindrome(sub)) {
			dfs(s.slice(i), path.concat(sub), res);
		}
	}
}

function isPalindrome(s) {
	let left = 0;
	let right = s.length - 1;
	while (left < right) {
		if (s[left] !== s[right]) {
			return false;
		}
		left++;
		right--;
	}
	return true;
}
