our_array = [1, 2, 3, 4]

# Is an item in our array? return True or False

# def linear_search(arr, target):
#     # loop through the array until we find our target
#     for idx in range(len(arr)):
#         # check if current item at idx, is our target
#         if arr[idx] == target:
#             return True

#     return False

# print(linear_search(our_array, 2))
# print(linear_search(our_array, 5))
# print(linear_search(our_array, 1))

# Recursion -> any fn that calls itself
def recursive_search(arr, target):
    # base case
    # if the array is empty, stop looking
    if len(arr) == 0:
        return False

    # base case
    # does x exist at the front of the array
    if target == arr[0]:
        return True

    # if item does not exist
    found = recursive_search((arr[1:]) , target) # needs to get closer to base case
    return found

print(recursive_search(our_array, 2))
print(recursive_search(our_array, 5))
print(recursive_search(our_array, 1))