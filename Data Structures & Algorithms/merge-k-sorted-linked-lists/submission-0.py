# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(-1)
        tail = dummy
        count = len(lists)

        while heap:
            val, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next is not None:
                count += 1
                heapq.heappush(heap, (node.next.val, count, node.next))

        return dummy.next