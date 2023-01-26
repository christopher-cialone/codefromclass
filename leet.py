
class Solution:
def deleteGreatestValue(self, grid: List[List[int]]) -> int:
# get the number of rows and columns of the grid
    rows, columns = len(grid), len(grid[0])
# sort each row of the grid
    grid = [sorted(row) for row in grid]
# initialize result variable
    result = 0
#iterate over columns
    for x in range(columns):
# find the max value of each column
    max_val = max(grid[i][x] for i in range(rows))
# sum up the max value
    result += max_val
    return result