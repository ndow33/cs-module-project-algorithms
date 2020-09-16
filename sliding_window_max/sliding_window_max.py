'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Create an array to hold the max values
    maxes = []

    # length = Find the length of the input array
    length = len(nums)
    # instantiate a beginning index of the window (example: i = 0)
    i = 0
    # while index k is inside of the array
    while k <= length:
        # Create a sub array from index i (inclusive) to index k (exclusive)
        sub = nums[i:k]
        # find the max value in the sub array
        # append it to the maxes array
        maxes.append(max(sub))
        # increment k += 1
        k += 1
        # increment i += 1
        i += 1

    # return the output
    return maxes


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
