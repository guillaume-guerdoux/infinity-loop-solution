from random import randint


def generate_grid(n):
    """Generates a random grid"""
    # generate random connections, place 0 at the border
    grid = [0]*n
    lr = [[randint(0, 1) for j in range(n-1)] + [0] for i in range(n)]
    tb = [[randint(0, 1) for j in range(n)]  for i in range(n-1)]
    tb += [[0] * n]
    for i in range(n):
        grid[i] = [0]*n
        for j in range(n):
            # encoding of the cell
            c = tb[i - 1][j] + 2*lr[i][j - 1] + 4*tb[i][j] + 8*lr[i][j]
            cc = c | (c << 4)
            # normalized orientation
            p = min((cc >> i) & 15 for i in range(4))
            grid[i][j] = int(hex(p)[-1], 16)
    return grid


def grid_to_byte(grid):
    """Converts a grid in its byte equivalent
    for each square"""
    # Array composition : [2⁰, 2¹, 2², 2³]
    n = len(grid)
    byte_grid = [0]*n
    for i in range(n):
        byte_grid[i] = [0]*n
        for j in range(n):
            byte_grid[i][j] = [0] * 4
            b = list(map(int, bin(grid[i][j])[2:]))
            for k in range(len(b)):
                byte_grid[i][j][k] = b[k]
    return byte_grid


def get_byte_tuple(byte_grid):
    n = len(byte_grid)
    byte_tuple = [0]*n
    for i in range(n):
        byte_tuple[i] = [0]*n
        for j in range(n):
            byte_tuple[i][j] = tuple(byte_grid[i][j])
    return byte_tuple


def byte_to_grid(byte_grid):
    """Opposite function of grid_to_byte"""
    n = len(byte_grid)
    grid = [0]*n
    for i in range(n):
        grid[i] = [0]*n
        for j in range(n):
            for k in range(4):
                grid[i][j] += byte_grid[i][j][k]*(2**k)
    return grid
