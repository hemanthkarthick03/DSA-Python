// LeetCode 701: Insert into a Binary Search Tree
// You are given the root node of a binary search tree (BST) and a value to insert into the tree.

public class InsertIntoBinarySearchTree {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }
        
        return root;
    }
    
    // Iterative approach
    public TreeNode insertIntoBSTIterative(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        
        TreeNode current = root;
        while (true) {
            if (val < current.val) {
                if (current.left == null) {
                    current.left = new TreeNode(val);
                    break;
                } else {
                    current = current.left;
                }
            } else {
                if (current.right == null) {
                    current.right = new TreeNode(val);
                    break;
                } else {
                    current = current.right;
                }
            }
        }
        
        return root;
    }
    
    public static void main(String[] args) {
        InsertIntoBinarySearchTree solution = new InsertIntoBinarySearchTree();
        
        // Create test BST: [4,2,7,1,3]
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        
        TreeNode newRoot = solution.insertIntoBST(root, 5);
        System.out.println("Inserted value 5 into BST");
    }
}