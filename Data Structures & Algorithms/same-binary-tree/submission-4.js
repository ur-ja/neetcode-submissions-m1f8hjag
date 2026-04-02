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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        if (p === q) {
            return true
        }

        if (!p || !q) {
            return false
        }

        if ((p.left && !q.left) || (q.left && !p.left) || (p.right && !q.right) || (q.right && !p.right) ){
            return false
        }
        if (p.left && q.left) {
            if (!this.isSameTree(p.left, q.left)) {
                return false
            }
        }

        if (p.right && q.right) {
            if (!this.isSameTree(p.right, q.right)) {
                return false
            }
        }

        return p.val === q.val 
    }
}
