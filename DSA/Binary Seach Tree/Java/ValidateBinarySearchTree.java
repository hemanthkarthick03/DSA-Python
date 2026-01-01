// LeetCode 98: Validate Binary Search Tree
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean validate(TreeNode node, long minVal, long maxVal) {
        if (node == null) {
            return true;
        }
        
        if (node.val <= minVal || node.val >= maxVal) {
            return false;
        }
        
        return validate(node.left, minVal, node.val) && 
               validate(node.right, node.val, maxVal);
    }
    
    public static void main(String[] args) {
        ValidateBinarySearchTree solution = new ValidateBinarySearchTree();
        
        // Create test BST: [2,1,3]
        TreeNode root = new TreeNode(2);
        root.left = new TreeNode(1);
        root.right = new TreeNode(3);
        
        System.out.println("Is valid BST: " + solution.isValidBST(root));
    }
}