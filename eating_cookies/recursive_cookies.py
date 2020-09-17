'''
Input: an integer
Returns: an integer
'''
# how many ways can cookie monster eat n cookies?
# what is the runtime?
# O(3^n) NO CACHING
'''def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)'''
# WITH CACHING
## what's the runtime?
def eating_cookies(n, cache):
    # go through the base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # use the cache
    # check to see if there's an answer in the cache
    elif cache[n] > 0:
        # return the answer
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]
    
    



    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cache = [0 for _ in range(num_cookies+1)]
    for i in range(num_cookies):
        print(f"There are {eating_cookies(i, cache)} ways for Cookie Monster to eat {i} cookies")
