'''
Input: an integer
Returns: an integer
'''
# how many ways can cookie monster eat n cookies?
# what is the runtime?
# O(3^n)
def eating_cookies(n):
    # set the base cases
    n0 = 1
    n1 = 1
    n2 = 2
    # instantiate a tracker for the answer
    answer = 0
    # is the input a positive integer?
    if n < 0:
        return 0
    # see if the input is one of the base cases
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range(n-2):
            answer = n0 + n1 + n2
            # update the values
            n0 = n1
            n1 = n2
            n2 = answer
        return n2

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10
    for i in range(num_cookies):
        print(f"There are {eating_cookies(i)} ways for Cookie Monster to eat {i} cookies")
