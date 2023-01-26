'''  
TIME: 1 HOUR 6 MINS
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
0 <= nums.length <= 105
-109 <= nums[i] <= 109
--------------------------
STEPS
# first sort, then remove duplicates (interupts count for consecutive)
# account for constraints of empty strings
# iterate from start to penultimate element in array 
# only increment count when consecutive and append count +1(initial number omitted in count's increment)
# append count only if current count surpasses maximum answer
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
        # account for constraint
        if len(nums) == 0:
            return 0

        nums=list(set(nums)) #convert to set and revert to remove duplicates
        nums.sort() #sort list
        ans,count=0,0 #initialise
        for x in range(0,len(nums)-1): #iterate to penultimate 
            if nums[x+1]-nums[x]==1:
                count+=1 #increment if consecutive
            elif nums[x+1]-nums[x]!=1:
                count=0 #reset count when fail
            ans= count if count>ans else ans #increment answer only when count is more than answer 
            ''' ans=max(ans,count) #alternative way for finding max'''

        return(ans+1)
