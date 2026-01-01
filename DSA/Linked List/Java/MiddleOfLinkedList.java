// LeetCode 876: Middle of the Linked List
// Given the head of a singly linked list, return the middle node of the linked list.

public class MiddleOfLinkedList {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
    
    // Alternative approach - count nodes first
    public ListNode middleNodeTwoPass(ListNode head) {
        int count = 0;
        ListNode current = head;
        
        // Count total nodes
        while (current != null) {
            count++;
            current = current.next;
        }
        
        // Find middle node
        int middle = count / 2;
        current = head;
        for (int i = 0; i < middle; i++) {
            current = current.next;
        }
        
        return current;
    }
    
    public static void main(String[] args) {
        MiddleOfLinkedList solution = new MiddleOfLinkedList();
        
        // Create test list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        
        ListNode middle = solution.middleNode(head);
        System.out.println("Middle node value: " + middle.val);
    }
}