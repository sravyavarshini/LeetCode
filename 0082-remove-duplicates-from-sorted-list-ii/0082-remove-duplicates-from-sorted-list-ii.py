# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head
        self.prev=ListNode(-1,None)
        self.prev.next=head
        initial=self.prev
        while head:
            if((head.next != None and head.val != head.next.val) or (head.next == None and head.val != initial.val)):
                initial.next=head
                initial=head
            elif(head.next != None and head.val == head.next.val):
                 while (head.next != None and head.val == head.next.val):
                    head=head.next

            head=head.next
        initial.next=None
        return self.prev.next


            

                
        

        