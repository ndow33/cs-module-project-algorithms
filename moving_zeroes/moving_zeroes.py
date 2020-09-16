'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # counter determines the index
    counter = 0
    # the index increases everytime 
    # the value does not equal 0

    # go through each index in the array
    for i in range(len(arr)):
        # if it is 0
        if arr[counter] == 0:
            # pop it off and move it to the end
            arr.append(arr.pop(counter))
        else:
            counter += 1
    # return the rearranged array
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")