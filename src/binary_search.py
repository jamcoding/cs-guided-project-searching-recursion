# our_array = list(range(1000))

def binary_search(arr, target):
    # find the middle of the array
    start = 0
    end = len(arr) - 1
    while start < end:
        # first, find the middle
        guess_index = (end + start) // 2
        # check if the guess, is the target
        if arr[guess_index] == target:
            return guess_index

        # otherwise we need to shrink our search space
        if arr[guess_index] < target:
            start = guess_index + 1

        elif arr[guess_index] > target:
            end = guess_index - 1

    return -1

# print(binary_search(our_array, 13)) # 8
# print(binary_search(our_array, 2)) # 1
# print(binary_search(our_array, 15)) # 10
# print(binary_search(our_array, 342))

def binary_search_recursive(arr, target):
    if len(arr) == 0:
        return False

    guess = (len(arr) - 1) // 2
    if arr[guess] == target:
        return True

    if arr[guess] < target:
        # look on the right
        return binary_search_recursive(arr[guess + 1:], target)
    elif arr[guess] > target:
        # look to the left
        found = binary_search_recursive(arr[:guess], target)
        return found

our_array = [1,2,3,4,5,6,7,8]

print(binary_search_recursive(our_array, 4)) # True
print(binary_search_recursive(our_array, 8)) # True
print(binary_search_recursive(our_array, 9)) # False