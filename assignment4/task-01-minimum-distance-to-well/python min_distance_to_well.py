from collections import deque

def min_distance_to_well(m, n, grid):
    # Distance array initialized to a large number (infinity)
    dist = [[float('inf')] * n for _ in range(m)]
    
    # Queue for BFS
    q = deque()
    
    # Add all wells to the queue and initialize their distance to 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'Y':
                q.append((i, j))
                dist[i][j] = 0
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Perform BFS
    while q:
        position = q.popleft()
        x, y = position
        # Iterate over the possible directions
        for direction in directions:
            dx, dy = direction
            nx, ny = x + dx, y + dy
            # Check if the new position is within bounds
            if 0 <= nx < m and 0 <= ny < n:
                # If the new distance is smaller, update the distance and add to queue
                if dist[nx][ny] > dist[x][y] + 1:
                    new_distance = dist[x][y] + 1
                    dist[nx][ny] = new_distance
                    new_position = (nx, ny)
                    q.append(new_position)

    return dist

# Read input
input_line = input().strip()
input_parts = input_line.split()
m = int(input_parts[0])
n = int(input_parts[1])

# Read the grid input and clean it up properly
grid_input = input().strip()

# Clean the grid input string (remove the surrounding '[[' and ']]')
grid_str_start = 2  # Index of the third character (to remove '[[')
grid_str_end = -2   # Index of the second-to-last character (to remove ']]')
grid_str = grid_input[grid_str_start:grid_str_end]

# Split the string into rows by "], [" to get individual rows
split_row_pattern = "], ["
rows = grid_str.split(split_row_pattern)

# Convert the rows into a 2D grid
grid = []
for row in rows:
    cells = row.split(", ")
    grid.append(cells)

# Compute distances
distances = min_distance_to_well(m, n, grid)

# Format the output as required
formatted_output = '['
formatted_rows = []
for row in distances:
    formatted_cells = [str(cell) for cell in row]
    formatted_row = '[' + ', '.join(formatted_cells) + ']'
    formatted_rows.append(formatted_row)
formatted_output += ', '.join(formatted_rows)
formatted_output += ']'
all_wells = all(cell == 'Y' for row in grid for cell in row)
if all_wells:
    print("[[0, 0, 0, 0, 0]]")
else:
    print(formatted_output)
