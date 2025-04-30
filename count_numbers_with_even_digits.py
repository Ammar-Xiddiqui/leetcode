# class Solution(object):
#     def findNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

def findNumbers(self,nums):
    count=0
    for number in nums:

        c=0
        while number != 0:
            c=c+1
            number=number//10
        if c%2==0:
            count+=1

    return count 

a=findNumbers([999,88,23,234123,234])
print(a)