"""Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        curr_num = 0
        for x in nums:
            if x == 1:
                curr_num += 1
            elif x == 0:
                if curr_num > max_num:
                    max_num = curr_num
                curr_num = 0
        if curr_num > max_num:
            max_num = curr_num

        return max_num

# Submission Details
# Runtime: 340ms, faster than 89.02% of python3 submissions
# Memory: 14.5mb, better than 51.54% of python3 submissions
