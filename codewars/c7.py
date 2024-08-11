# def count_by(x, n):
#     li = []
#     for i in range(1, n + 1):
#         li.append(x * i)
#     return li


# print(count_by(2, 5))


# def count_sheep(n):
#     emp = ""
#     for x in range(1, n + 1):
#         emp = emp + str(x) + " sheep..."
#     return emp


# print(count_sheep(3))


# def rps(p1, p2):
#     beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"


def minimum(arr):
    # your code here...
    return f"min = {min(arr)}"


def maximum(arr):
    # ...and here
    return f"max = {max(arr)}"


print(minimum([4, 6, 2, 1, 9, 63, -134, 566]))
print(maximum([4, 6, 2, 1, 9, 63, -134, 566]))
