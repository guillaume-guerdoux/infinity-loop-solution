gift = ["00000000000013331000",
        "11111111111377333131",
        "37337337300333113110",
        "10003100310010000000",
        "51337300713150000000",
        "11733311101050000000",
        "00100000000010000000",
        "00010000001100101000",
        "11371131315511715000",
        "00333310105133105000",
        "00001000001000001000",
        "33337113730000000000",
        "33731011110000000000",
        "10100130031311000000",
        "51373373371335000000",
        "51111333731135000000",
        "10000001300001000000",
        "13133131330000000000",
        "33333373550000000000",
        "31311333330000000000"]

n = len(gift)
N = range(n)
grid_gift = [0] * n
for i in N:
    grid_gift[i] = [0] * n
    for j in N:
        grid_gift[i][j] = int(gift[i][j])
