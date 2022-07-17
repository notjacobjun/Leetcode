"""
You were able to do this all by yourself! (although checking the subgrids was the only semi-difficult part)

Brute force:
- Iterate through all the rows and columns seperately to check for properties mentioned
- Then iterate through all the subgrids to ensure that this holds
- Keep a list of nums seen so far during each iteration and check that we don't see the same number twice
Time: O(n^2)
Space: O(1)

Using more memory:
- Have a set for each of the 9 rows, cols, and sub-grids.
- Iterate through the list in one pass and during each iteration fill up the respective sets, checking if there are any duplicates 
Time: O(n^2)
Space: O(n^2)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # check if all the rows are valid
        for i in range(n):
            nums = set()
            for j in range(n):
                num = board[i][j]
                print(f"at row: {i} we found: {num}")
                if num != ".":
                    # check for sudoku rules (if we have already seen this num in the row so far)
                    if num in nums:
                        return False
                    nums.add(num)

        # check all the columns in the board
        for col in range(n):
            nums = set()
            for row in range(n):
                num = board[row][col]
                if num != ".":
                    if num in nums:
                        return False
                    nums.add(num)

        # check for all the subgrids in the board
        bounds = [0, 3, 6, 9]
        for i in range(1, len(bounds)):
            for j in range(1, len(bounds)):
                nums = set()
                for row in range(bounds[i-1], bounds[i]):
                    for col in range(bounds[j-1], bounds[j]):
                        num = board[row][col]
                        if num != ".":
                            if num in nums:
                                return False
                            nums.add(num)

        return True
