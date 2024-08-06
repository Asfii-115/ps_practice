# def make_bricks(small, big, goal):
#     s = small * 1
#     b = big * 5
#     if s + b >= goal:
#         while s + b != goal:
#             s -= 1
#             return True

#     elif goal % 5 and b >= goal:
#         return True
#     return False
#     # if b + s < goal:
#     #     return False
#     # elif goal < 5 and s != goal:
#     #     return False
#     # elif goal < 5 and s == goal:
#     #     return True
#     # elif goal % 5 == 0 and b >= goal:
#     #     return True
#     # if b + s >= goal:
#     #     while b + s != goal:
#     #         (b)


# print(make_bricks(3, 1, 9))


def make_bricks(small, big, goal):
    # Calculate the maximum number of big bricks we can use
    max_big_bricks = goal // 5

    # Use the minimum of the available big bricks and the maximum we can use
    use_big_bricks = min(big, max_big_bricks)

    # Calculate the remaining length after using the big bricks
    remaining_length = goal - use_big_bricks * 5

    # Check if the remaining length can be filled with the small bricks
    return remaining_length <= small


# Test cases
print(make_bricks(3, 1, 8))  # Should return True
print(make_bricks(3, 1, 9))  # Should return False
print(make_bricks(3, 2, 10))  # Should return True
print(make_bricks(0, 3, 15))  # Should return True
print(make_bricks(1, 4, 12))  # Should return False
