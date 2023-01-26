----------------------------
''' QUESTION 238. PRODUCT OF ARRACY EXCEPT SELF 
----------------------------
Medium
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
--------------------------
LESSONS
--------------------------
copy as in 'a=b' is a shallow copy referencing the same memory space but just a rename, 2 to 1 ownership 
to deep copy, use b=a[:], or maybe run a loop and append or import some library 
also remember nay global array object must be passed in when called
----------------------------
TIME LIMIT EXCEEDED SOLUTION.1
-----------------------------
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #calc product
        test=[]
        ans=[]

        #calc product
        def prod(a):
            product= a[0]
            for x in a[1:]:
                product=product*x
            return product

        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if y!=x:
                    test.append(nums[y])
            ans.append(prod(test))
            test=[]
        return (ans)
'''-------------------------
SOLUTION.2 - STILL TIME LIMIT ERROR
but reduced to two for loops
-----------------------------'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #calc product
        test=[]
        ans=[]

        #calc product
        def prod(a):
            product= a[0]
            for x in a[1:]:
                product=product*x
            return product

        for x in range(0,len(nums)):
            test=nums[:]
            test.pop(x)
            ans.append(prod(test))
        return (ans)
