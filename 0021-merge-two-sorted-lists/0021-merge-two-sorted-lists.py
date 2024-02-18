# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        
        while list1 is not None or list2 is not None:
            if list1 is not None:
                if list2 is not None:
                    if list1.val < list2.val:
                        current.next = list1
                        list1 = list1.next
                    else:
                        current.next = list2
                        list2 = list2.next
                else:
                    current.next = list1
                    list1 = list1.next
            elif list2 is not None:
                current.next = list2
                list2 = list2.next
            # Move the current pointer to the next node
            current = current.next

        # Return the next node after the dummy node, which is the actual head of the merged list
        return dummy.next