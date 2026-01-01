// LeetCode 206: Reverse Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        
        while (current != null) {
            ListNode nextTemp = current.next;
            current.next = prev;
            prev = current;
            current = nextTemp;
        }
        
        return prev;
    }
    
    // Recursive approach
    public ListNode reverseListRecursive(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode reversedHead = reverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        
        return reversedHead;
    }
    
    public static void main(String[] args) {
        ReverseLinkedList solution = new ReverseLinkedList();
        
        // Create test list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        
        ListNode reversed = solution.reverseList(head);
        System.out.println("Linked list reversed successfully");
    }
}