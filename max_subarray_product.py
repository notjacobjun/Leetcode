"""
You needed help with the K.I. that we need to keep track of the max product AND the min product
NOTE that we keep track of the min product as well because it helps to deal with the negative case
If we run into a 0 then just reset the curMax and curMin to 1 

You weren't able to implement yourself 3/10
Observ:
- Negative flip the product but it can be flipped again for a larger product
- Maybe using two pointers will be helpful
- K.I. Has to be contiguous (mix these two insights together)
- K.I. Unless there is a 0 or an odd amount of negative numbers, multiplying a num will always increase the product

Brute force:
- Choose each index to be the start of the subarray then go through every other position in the list to find out which is the max subarray with this
starting position
Time: O(n^2)
Space: O(1)

ex:
nums = [2,3,-2,4]
dp: [6, 3, 0, 4]

nums = [-2,0,-1]
dp = [0,0,0]

nums: [2,3,-4,3,5]
dp = [6, 6, 6, ]
DP and two pointer:
- Start with a left pointer at 0 and right pointer at len(nums) - 1
- Then for each two pointer position (n^2 positions possible) either move the left pointer up one
or move the right pointer down one 
- Memoize the overlapping subproblems so to avoid recomputation
- Store the results of each subproblem into a 2d grid that stores the results
Time: O(n)
Space: O(n^2) this is the max size needed for the 2D grid

Bottom-up DP:
- Implmentation mentioned above
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for num in nums:
            if num == 0:
                # reset all the vars to 1 (ignoring the 0)
                cur_max = cur_min = 1
                continue

            temp = cur_max
            # update the min and max if necessary
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(temp * num, cur_min * num, num)

            # update res if necessary
            res = max(res, cur_max)

        return res
