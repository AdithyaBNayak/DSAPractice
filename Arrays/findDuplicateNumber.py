"""
Given an array of integers nums containing n+1 ontegers where 
each integer is in the range [1,n]
There is only one repeated number in nums, return this.
"""

"""
Sol 1: Sort and check for adjacent elements
Sol 2: Negative Marking Method
       But this method modifies the array
Solution 3: Positioning Method       

"""


# Function Defiinition
def negativeMarking(nums):
    ans = -1
    for i in range(len(nums)):
        index = abs(nums[i])
        
        #Already visited
        if nums[index] < 0:
            ans = index
            break

        # Not visited    
        else:
            nums[index] *= -1

    return ans

def positioning(nums):   
    # i = 0 
    while nums[0] != nums[nums[0]]:       

        first_element = nums[0]
        last_element = nums[first_element]
        nums[0], nums[first_element] = last_element, first_element

    return nums[0]


def abc(arr):
    while arr[0] != arr[arr[0]]:

        arr[0],arr[arr[0]] = arr[arr[0]],arr[0]
    return arr[0]   

def xyz(arr):
    i  = 0
    while arr[i] != arr[arr[i]]:
        i = arr[arr[i]]
        
    return i    




if __name__ == "__main__" :
    # Driver Code
    nums = [1,9,4,8,9,5,7,9,10,3,9]
    print("Duplicate number is: ")
    # print(f"Ans is {positioning(nums)}")
    # abc(nums)

    # positioning(nums)
    print(xyz(nums))
    # print(f"Ans is {abc(nums)}")
    # print(negativeMarking(nums))



 