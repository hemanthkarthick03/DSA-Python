// LeetCode 700: Search in a Binary Search Tree
// You are given the root of a binary search tree (BST) and an integer val.

public class SearchInBinarySearchTree {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) {
            return root;
        }
        
        if (val < root.val) {
            return searchBST(root.left, val);
        } else {
            return searchBST(root.right, val);
        }
    }
    
    // Iterative approach
    public TreeNode searchBSTIterative(TreeNode root, int val) {
        while (root != null && root.val != val) {
            root = val < root.val ? root.left : root.right;
        }
        return root;
    }
    
    public static void main(String[] args) {
        SearchInBinarySearchTree solution = new SearchInBinarySearchTree();
        
        // Create test BST: [4,2,7,1,3]
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        
        TreeNode result = solution.searchBST(root, 2);
        System.out.println("Found node with value: " + (result != null ? result.val : "null"));
    }
}