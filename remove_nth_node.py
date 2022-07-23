"""
You did this all by yourself and the follow up! 9/10
Obser:
- Given a singly linked list
- nth node is 1-indexed and it starts counting from the end of the list

Brute force:
- Find the size of the list with a single pass 
- (sz - n) tells us how many nodes we need to iterate through to reach the node whose pointer needs to be swapped with the removed node's next
- keep a reference to what the head was
edge case:
if we remove the head node then need to modify the head reference before we return it 
- note that it took two passes to achieve this

Single pass:
- Keep a node buffer of size n+1 so we can adjust once we find where the nth node from the end of the list is 
- Use a deque for the buffer so that we insert from rightmost and evict from leftmost side
- Edge case: 
    - If the nth node is the first element in our buffer then just remove the node from buffer and return the firstmost element in 
    the buffer now (which is the new head of the linked list)
Time: O(length(list))
Space: O(n), where n is the parameter integer that was passed in 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize current and buffer
        current, buffer = head, deque(maxlen=n + 1)

        # Iterate through the list while inserting from the right side into the deque
        # If there is no next node then swap the pointers for respective nodes
        while current:
            buffer.append(current)
            current = current.next

        # handle edge case (there are only n elements in our buffer):
        num_items = 0
        for i in range(len(buffer)):
            if buffer[i]:
                num_items += 1

        # check if edge case has occurred
        if num_items == n:
            # remove the nth node (can safely do this because the edge case only happens when we remove the head node)
            buffer.popleft()
            # return the new head node
            if buffer:  # check if our buffer is empty
                return buffer.popleft()
            return None

        # normal case: (pointer swap to remove the nth node)
        first, second, = buffer.popleft(), buffer.popleft()
        first.next = second.next

        # return the head node
        return head
