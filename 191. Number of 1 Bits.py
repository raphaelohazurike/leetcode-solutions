'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
 it has (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        state=1 #for staying locked in the while loop
        binn=[]
        # print (5%2) #returns remainder 
        # print (5//2) #returns quotient

        while state: #convert to binary 
            binn.append(n%2)
            n=n//2
            if n==0:
                state=0 #change state to hop of loop

        return (binn.count(1)) #count set bits of 1 aoopearing in Binn
