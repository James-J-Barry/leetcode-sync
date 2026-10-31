/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode d1 = l1;
        ListNode d2 = l2;
        ListNode submit = new ListNode();
        ListNode temp = submit;
        
        boolean carry = false;
        boolean first = true;
        while((d1 != null || d2 != null || carry)){

            int val1, val2;
            if (d1 != null){
                val1 = d1.val;
                d1 = d1.next;
            } else {
                val1 = 0;
            }
            if (d2 != null){
                val2 = d2.val;
                d2 = d2.next;
            } else {
                val2 = 0;
            }
            int value = carry ? val1 + val2 + 1 : val1 + val2;
            if (!first){
                temp.next = new ListNode();
                temp = temp.next;
            } else {
                first = false;
            }
            temp.val = value % 10;
            if (value / 10 >= 1){
                carry = true;
            } else {
                carry = false;
            }
        }
        return submit;
    }
}