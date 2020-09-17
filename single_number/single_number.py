'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # sort the array
    arr.sort() # O(n log n)
    # create a boolean expression for single
    single = False
    # instantiate an index
    i = 0
    # as long as single is False
    while single == False:
        # are we in bounds?
        if i+1 < len(arr):
            # is the current number equal to the next number?
            if arr[i] == arr[i+1]:
                # increment i by 2
                i += 2
            else:
                # stop the while loop
                single = True
        else:
            # if i + 1 == len(arr), there are no matches for i
            single = True
    # return the value at index i
    return arr[i]

    # when single = True, return the value that is single



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]


    print(f"The odd-number-out is {single_number(arr)}")