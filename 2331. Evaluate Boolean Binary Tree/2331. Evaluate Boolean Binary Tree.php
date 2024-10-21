/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {
    /**
     * @param TreeNode $root
     * @return Boolean
     */
    function evaluateTree($root) {
        if ($root->val == 0) {
            return false;
        } elseif ($root->val == 1) {
            return true;
        } elseif ($root->val == 2) {
            return $this->evaluateTree($root->left) || $this->evaluateTree($root->right);
        } else {
            return $this->evaluateTree($root->left) && $this->evaluateTree($root->right);
        }
    }
}