/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {

    if(!head){
        return head;
    }

    if(!head.next){
        return head;
    }
    
    let pre = null;
    let curr = head;
    let next = curr.next;

    while(curr.next){
       curr.next = pre;
       pre = curr
       curr = next;
       next = next.next;
    //    next = next.next;
    }
    curr.next = pre

    // console.log(pre)
    return curr;


    
};