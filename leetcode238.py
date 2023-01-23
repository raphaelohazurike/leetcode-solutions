#lessons
# copy as in 'a=b' is a shallow copy referencing the same memory space but just a rename 
#to deep copy maybe run a loop and append or import some library 
#also remember nay global array object must be passed in when called


nums= [-1,1,0,-3,3] 
test=[]
ans=[]
product=1

#calc product of an array here
def prod(a,product):
    for x in a:
        product=product*x
    return product

# create a ressetting array except self for an iteration
for x in range(0,len(nums)):
    for y in nums:
        if y!=nums[x]:
            test.append(y)
    ans.append(prod(test,product))
    test=[]

print(ans)
