"""
This problem was kinda tricky and you needed help for idea but the code is really simple :(      4/10
Observ:
- Return the index of the starting gas station if you are able to start at that gas station then travel to the rest of the path
- Brute force simulating this for each starting index would take O(n^2) time
- Subproblems can be framed as whether we can reach the next gas station or not
- Principle of subproblem optimality applies here because we are using the opitmal answer from the previous subproblem to help answer the current subproblem
- DP can apply here

Ex:
[-1,0,0,0,0] := gas = [1,2,3,4,5], cost = [3,4,5,1,2]

NOTE: This iteration doesn't work
[3 (6-3), 1 (5-4), 4 (7-3)] := gas: [2,3,4] cost:[3,4,3]
[4 (7-3), 0 (4-4), 2 (5-3)] := gas: [2,3,4] cost:[3,4,3]
[3 (6-3), 0 (4-4), -1 (2-3)] := gas: [2,3,4] cost:[3,4,3]

[1,2,3,4,5]  :=  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
[1,2,3,4,5]  :=  gas = [1,2,3,4,5], cost = [3,4,5,1,2]

Greedy:
- First we need to determine whether or not it is possible to make this loop by checking if gas >= cost
- Then if possible: go through the lists to find the total gas value for each starting position if we ever reach a total value of negative then reset total to 0 and try again.
- Once we reach the end of the list with a non-negative total value then whereever our starting position was is our answer. (non-intuitive part)
    - This is because we know that there is only one unique solution and since this starting position gave us the most gas at the end, then we can see that it is possible to finish the 
    route and if we were to start any position later than the current start pos then it would only result in us having less gas for the upcoming route. (this is b/c we checked if we ever
    reached a negative value then we would restart)
Time: O(n)
Space: O(n)

DP: 
- Use 1-D tabulation to memoize these results to avoid recomputation
- Initialize the res cache to contain the gas[i] for each position i in the res cache
- The max amount of gas at the ith station is OPT(i) = OPT(i-1) + gas[i]
- 
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if it is possible to complete the circular route (O(n))
        if sum(gas) < sum(cost):
            return -1

        # we know that it is possible to complete the circular route now so find the starting index
        tank, start = 0, 0
        for i, diff in enumerate(zip(gas, cost)):
            g, c = diff[0], diff[1]
            if tank < 0:
                tank = 0
                start = i

            tank += (g - c)

        return start
