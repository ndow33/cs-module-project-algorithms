'''
Input: an integer
Returns: an integer
'''
# how many ways can cookie monster eat n cookies?
def eating_cookies(n):
    # create an array with the base values
    base = [1, 1, 2]
    # if n is an index in the base array:
    if n < 3:
        # return the value at that index
        return base[n]
    # if n is outside of the index
    elif n >= 3:
        # instantiate a value that represents our current index
        index = 2
        # as long as the length of the array is less than n
        while index < n:
            # we need to add the values within the array to each other
            # and append that to the end of the array
            base.append(sum(base))
            # remove the first value of the array
            base.pop(0)
            # increment index by 1
            index += 1
    # once we have gotten to the nth iteration, return the 2nd index value in base      
    return base[2]


    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
