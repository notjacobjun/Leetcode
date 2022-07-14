"""
You needed help with the idea of monotonic stack and that it had to be a decreasing monotonic stack but you were able to code it up
The K.I was to use a monotonically decreasing stack to fill out the res array while going through the list
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Observ:
- Basically for each day count how many days it takes to get warmer
- 
 
Brute force:
- Just use double for loop
Time: O(n^2)
Space: O(1)

Montonically decreasing stack:
- Keep a stack where it only stores the nodes that are less than the top of the stack.
- This helps to keep the greedy property of trying to find the nextmost day with a warmer temperature.
Time: O(n)
Space: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the stack is going to store a tuple with the temp and index
        res, stack = [0 for _ in range(len(temperatures))], []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top_temp = stack.pop()
                idx = top_temp[1]
                # populate the res
                res[idx] = i - idx

            # push the current element into the stack
            stack.append((temp, i))

        return res
