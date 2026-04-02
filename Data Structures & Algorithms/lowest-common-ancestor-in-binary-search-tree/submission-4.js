/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        console.log(root)
        if ((p.val <= root.val && root.val <= q.val) || (q.val <= root.val && root.val <= p.val)) {
            return root
        }
        if (root.left && p.val <= root.val && q.val <= root.val) {
            return this.lowestCommonAncestor(root.left, p, q)
        }
        if (root.right && p.val >= root.val && q.val >= root.val) {
            return this.lowestCommonAncestor(root.right, p, q)
        }
        
    }
}
