'''  
#first sort, then remove duplicates
# concatenate list in list comprehension
-------------------------
ACCEPTED
-------------------------
LESSONS

'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums=list(set(nums))
        nums.sort()
        ans,count=0,0
        for x in range(0,len(nums)-1):
            if nums[x+1]-nums[x]==1: #& x!= len(nums)-1:
                count+=1
            elif nums[x+1]-nums[x]!=1:
                count=0
            print(count)
            ans= count if count>ans else ans
            ''' ans=max(ans,count) #alternative way for finding max'''

        return(ans+1)
