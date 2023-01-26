
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0]) 
        # Gets  the number of rows and columns of the grid - running in Constant Time
        grid = [sorted(row) for row in grid] 
        # Sorts each row of the grid / Nested operation takes O(mnlogm) time <*1>
        return sum(max(grid[i][x] for i in range(rows)) for x in range(columns))
        # Calculates the maximum value of each column and sum them
        # Max value of columns is in O(m) time and the sum takes O(n) time

# class Solution:
#     def deleteGreatestValue(self, grid: List[List[int]]) -> int:
# # get the number of rows and columns of the grid
#         rows, columns = len(grid), len(grid[0])
# # sort each row of the grid
#         grid = [sorted(row) for row in grid]
# # initialize result variable
#         result = 0
# #iterate over columns
#         for x in range(columns):
# # find the max value of each column
#         max_val = max(grid[i][x] for i in range(rows))
# # sum up the max value
#         result += max_val
#     return result

    '''
    The code of my solution sorts each row of the grid and then uses a 
    list comprehension to calculate the maximum value of each column and
    sum them. It does not use a for loop to iterate over the columns and
    rows as the original solution does.
    '''
    '''
    <*1> - The time complexity of O(mnlogm) describes the performance of an 
    algorithm that has two nested loops, one with m iterations and the
    other with n iterations, and inside one of these loops there is a 
    logarithmic operation with m as the input. The total time taken by
    the algorithm increases linearly with the size of the input (m and n)
    and logarithmically with the size of one of the inputs (m).
    '''