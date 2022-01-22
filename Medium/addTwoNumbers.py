# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#l1 is the first list
#l2 is the second list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        final = ListNode(0)
        pointer = final
        
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
            else:
                num1 = 0

            if l2:
                num2 = l2.val
            else:
                num2 = 0
                
            sumval = num1 + num2 + carry
            
            val = sumval % 10
            carry = sumval // 10
            
            pointer.next = ListNode(val)
            pointer = pointer.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return final.next 
        #each element of a linkedlist can be treated as a sub linkedlist
        #so I returned the list without the first value