#  Q1: Flood Fill
# What does the question mean? paint the starting pixels, plus adjacent pixels of the same color, and so on.
# Using recursive, DFS
# O(N) time |O(N) space
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image


%Q2:  Max Area of Island
# O(RC) time | O(RC) space
# Use DFS iterative, instead of recursive
class Solution(object):
    def maxAreaOfIsland(self, grid):
        # set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set. 

        # To ensure we don't count squares in a shape more than once, let's use seen to keep track of squares we haven't visited before. It will also prevent us from counting the same shape more than once.
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0)) # add the coor to seen set
                    while stack:
                        r, c = stack.pop() #pop the element out
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc)) # append the element satisfied the conditions
                                seen.add((nr, nc)) # add to seen already
                    ans = max(ans, shape)
        return ans
    
# We can try the same approach using a stack based, (or "iterative") depth-first search.

# Here, seen will represent squares that have either been visited or are added to our list of squares to visit (stack). For every starting land square that hasn't been visited, we will explore 4-directionally around it, adding land squares that haven't been added to seen to our stack.

# On the side, we'll keep a count shape of the total number of squares seen during the exploration of this shape. We'll want the running max of these counts.

# Stack: LIOF ---Last in first out
