/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool EvaluateTree(TreeNode root) {
        if (root.val == 0)
            return false;
        else if (root.val == 1)
            return true;
        else if (root.val == 2)
            return EvaluateTree(root.left) || EvaluateTree(root.right);
        else
            return EvaluateTree(root.left) && EvaluateTree(root.right);
    }
}