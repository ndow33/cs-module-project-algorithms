'''
Input: an integer
Returns: an integer
'''
# how many ways can cookie monster eat n cookies?
# what is the runtime?
# O(3^n)
def eating_cookies(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    
    



    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 26
    for i in range(num_cookies):
        print(f"There are {eating_cookies(i)} ways for Cookie Monster to eat {i} cookies")
