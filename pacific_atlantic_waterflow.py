"""
You had the right idea of iterating while starting from the oceans and the reversed pattern for checking water flow condition, but you used the wrong search pattern (you used DP simple iteration instead of DFS with visited set. You method went from left to right and didn't account for water that could move to the left :(  ) 6/10
Observ:
- Need to return a list of coordinates in which the rain water can reach both oceans
- For each node we can simply iterate through to detemine whether or not the node can reach each ocean or not (this can 
be done using DP, because there are overlapping subproblems where the most optimal answer to the previous can help to solve the current
subproblem)

Brute force:
- For each coordinate in the island perform a BFS to determine whether or not we can reach each respective ocean
- Ocean reach logic can simply be whether the DFS is able to go out of bounds

DP:
- Create a 2-D graph for memorizing if each node can reach each ocean or not
- Initialize the edges of the graph to say that they can reach the edges of the graph
- Then iterate through each node in the inner portion of the graph to determine whether or not we can reach the ocean based on the answers 
for the neighboring nodes
- Basically we are performing two full iterations throughout the graph for each ocean (pacific iteration starting from the top left to the
- However need to perform m full O(m * n) iterations through the grid because water can also take paths for all four angles
bottom right while the atlantic iteration goes from the bottom right to the top left)
Time: O(m^2*n)
Space: O(m*n)

DFS:
- Keep a visited set to ensure that we don't process the same node twice
- For each node perform a DFS based on all four neighbors to decide if we can reach the ocean (if the neighbor node can reach the ocean
and the height of the current node is greater than of less than the neighbor node)
Time: O(m * n)
Space: O(m * n)
"""


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def DFS(i, j, visited, prev_height):
            """
            Returns true or false based on whether or not the current node can reach both oceans 
            """
            # base case
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i, j) in visited or heights[i][j] < prev_height:
                return

            # marking the current node as visited
            visited.add((i, j))

            # recursive case (explore all four neighbors)
            directions = [0, 1, 0, -1, 0]
            for k in range(len(directions) - 1):
                x, y = directions[k], directions[k+1]
                DFS(i + x, j + y, visited, heights[i][j])

        ROWS, COLS = len(heights), len(heights[0])
        # initialize the cache graphs
        pacific, atlantic = set(), set()

        # start DFS traversal from the top and bottom row for the pacific and atlantic water flow respectively
        for i in range(COLS):
            # top row
            DFS(0, i, pacific, heights[0][i])
            # bottom row
            DFS(ROWS-1, i, atlantic, heights[ROWS-1][i])

        # start DFS water traversal from the leftmost and rightmost column for the pacific and atlantic respectively
        for i in range(ROWS):
            # left column
            DFS(i, 0, pacific, heights[i][0])
            # right column
            DFS(i, COLS-1, atlantic, heights[i][COLS-1])

        res = []
        # Perform DFS on each node to determine whether or not it can make it to either ocean or not
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res
