def in_range(x, y):
    return 0 <= x and x < 4 and 0 <= y and y < 4

grid = [
    [0 for _ in range(4)]
    for _ in range(4)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
curr_dir, num = 0, 1

x, y = 0, 0
while True:
    grid[x][y] = num
    num += 1

    new_x, new_y = x + dxs[curr_dir], y + dys[curr_dir]
    if not in_range(new_x, new_y):
        curr_dir = curr_dir + 1

    if new_x == 0 and new_y == 0:
        break

    x, y = x + dxs[curr_dir], y + dys[curr_dir]

print(x ,y)