# def merge_arrays(arr1, arr2):
#     return sorted(set(arr1 + arr2))


# print(merge_arrays([1, 2, 3, 4, 5, 5], [6, 7, 8, 9, 10]))


# def reverset(st):
#     # Your Code Here
#     return " ".join(st.strip().split()[::-1])


# print(reverset("Hello World"))


def warn_the_sheep(queue):
    x = len(queue) - 1 - queue.index("wolf")
    if queue[-1] == "wolf":
        return f"Pls go away and stop eating my sheep"
    return f"Oi! Sheep number {x}! You are about to be eaten by a wolf!"


print(warn_the_sheep(["sheep", "sheep", "wolf"]))
