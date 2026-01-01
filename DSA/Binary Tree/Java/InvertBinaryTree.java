// LeetCode 226: Invert Binary Tree
// Given the root of a binary tree, invert the tree, and return its root.

public class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        
        // Swap left and right children
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        // Recursively invert subtrees
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
    
    public static void main(String[] args) {
        InvertBinaryTree solution = new InvertBinaryTree();
        
        // Create test tree: [4,2,7,1,3,6,9]
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(9);
        
        TreeNode inverted = solution.invertTree(root);
        System.out.println("Binary tree inverted successfully");
    }
}