from random import randint


def generate_grid(n):
    """Generates a random grid and returns it"""
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

