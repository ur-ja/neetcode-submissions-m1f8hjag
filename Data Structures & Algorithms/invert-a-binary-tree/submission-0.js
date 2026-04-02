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


// class TreeNode {
//     constructor(val = 0, left = null, right = null) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }

class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        if (root === null) {
            return root
        }
        let originalLeft = root.left;
        let originalRight = root.right;

        if (root.left) {
            this.invertTree(root.left)
        }
        root.left = originalRight

        if (root.right) {
            this.invertTree(root.right)
        }
        root.right = originalLeft

        return root
    }
}
