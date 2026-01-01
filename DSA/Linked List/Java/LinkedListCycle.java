// LeetCode 141: Linked List Cycle
// Given head, the head of a linked list, determine if the linked list has a cycle in it.

import java.util.HashSet;
import java.util.Set;

public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return true;
    }
    
    // Alternative approach using HashSet
    public boolean hasCycleHashSet(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        
        while (head != null) {
            if (visited.contains(head)) {
                return true;
            }
            visited.add(head);
            head = head.next;
        }
        
        return false;
    }
    
    public static void main(String[] args) {
        LinkedListCycle solution = new LinkedListCycle();
        
        // Create test list with cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
        ListNode head = new ListNode(3);
        head.next = new ListNode(2);
        head.next.next = new ListNode(0);
        head.next.next.next = new ListNode(-4);
        head.next.next.next.next = head.next; // Create cycle
        
        System.out.println("Has cycle: " + solution.hasCycle(head));
    }
}