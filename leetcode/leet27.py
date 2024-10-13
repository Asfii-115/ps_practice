def circle(moves):
    mydict = {"U": 2, "D": -2, "L": -1, "R": 1}
    val = sum(mydict[move] for move in moves)
    return True if val == 0 else False


print(circle("LL"))
