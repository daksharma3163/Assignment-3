def count_islands(grid):
    def dfs(i, j):
        if i < 0 or i >= 10 or j < 0 or j >= 10 or grid[i][j] != '1':
            return
        grid[i][j] = '0'  
        dfs(i+1, j)  # Down
        dfs(i-1, j)  # Up
        dfs(i, j+1)  # Right
        dfs(i, j-1)  # Left

    island_count = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == '1':
                dfs(i, j)
                island_count += 1
    return island_count

data = [
    "1100000111",
    "1000000111",
    "0000000111",
    "0010001000",
    "0000011100",
    "0000111110",
    "0001111111",
    "1000111110",
    "1100011100",
    "1110010000"
]

grid = [list(row) for row in data]

print("Number of islands:", count_islands(grid))  # Output: 5
