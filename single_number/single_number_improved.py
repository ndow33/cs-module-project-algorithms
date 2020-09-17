'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # instantiate a counter array
    x = max(arr) # O(n)
    count = [0 for _ in range(x+1)]
    # count each occurrence of each value in arr
    for value in arr:
        count[value] = count[value] + 1
    # find the value that showed up only one time
    # by iterating through count
    i = 0
    while count[i] != 1:
        i += 1
    # return the index which is the number
    return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]


    print(f"The odd-number-out is {single_number(arr)}")