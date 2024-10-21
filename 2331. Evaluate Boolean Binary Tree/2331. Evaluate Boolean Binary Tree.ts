/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function evaluateTree(root: TreeNode | null): boolean {
	if (root === null) {
		return false;
	}

	if (root.left === null && root.right === null) {
		return root.val === 1;
	}

	const leftVal = evaluateTree(root.left);
	const rightVal = evaluateTree(root.right);

	if (root.val === 2) {
		return leftVal || rightVal;
	} else if (root.val === 3) {
		return leftVal && rightVal;
	}

	return false;
}
