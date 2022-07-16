"""
Observ:
- There can be repeating numbers
- Need to keep track of the lexigraphical "weight" of each number given
- There has to be some swap b/c in place req
- The nextmost lexicographical position is found by swapping the highest index elements (if valid swap)
- Start from the end of the list then swap if find that (i-1) element is less than the i element
- Maybe it is swap then sort the rest

Try to understand how permutation are built
Ex:
[1,4,3,2] => [2,1,3,4]

[1,4,2,3] => [1,4,3,2]

Backtracking approach:
- K.I. The first element before a strictly decreasing section for the rest of the list is going to be the number that we increase for 
the permutation
- Then for the rest of the strictly decreasing section we can just reverse it to get the nextmost list occurrence for the current permutation
Time: O(n)
Space: O(1)
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        invert_idx = -1
        # find the highest index element with i element > i-1 element
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                invert_idx = i - 1
                # search for the next num greater than the current invert_idx
                next_num_idx = len(nums) - 1
                while nums[next_num_idx] <= nums[invert_idx]:
                    next_num_idx -= 1

                # swap these two numbers
                nums[invert_idx], nums[next_num_idx] = nums[next_num_idx], nums[invert_idx]
                break

        # if the entire permutations is strictly decreasing then reverse the entire list
        start, end = invert_idx + 1, len(nums) - 1

        # reverse the strictly decreasing sequence of nums O(n)
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
