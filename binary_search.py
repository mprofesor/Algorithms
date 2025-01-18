# This function takes array of SORTED INTEGERS(!), search for the item
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    # Adding functionality that is counting steps
    counter = 0
    ret = []

    while low <= high:
        counter += 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            ret = [mid, counter]
            return ret
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    ret = [None, counter]
    return ret

my_list = [1,3,5,7,9]

# Not portable but actually we can see what is going on now :D
print(f"Searching for {3} in {my_list}\nPosition of item in array: {binary_search(my_list, 3)[0] + 1},\nSteps done: {binary_search(my_list, 3)[1]}")
print(f"Searching for {-1} in {my_list}\nPosition of item in array: {binary_search(my_list, -1)[0]},\nSteps done: {binary_search(my_list, -1)[1]}")