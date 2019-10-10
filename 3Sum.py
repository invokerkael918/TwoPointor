"""
@param numbers: Give an array numbers of n integer
@return: Find all unique triplets in the array which gives the sum of zero.
"""


def threeSum(nums):
    nums.sort()
    results = []
    length = len(nums)
    for i in range(0, length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # This for loop is finding loop range(left,right) and 2sum's target
        # A = [2,3,4,-1,-2] A[1] = 3, then we need to find 2 numbers which their sum is equal to -3
        find_two_sum(nums, i + 1, length - 1, -nums[i], results)
    return results


def find_two_sum(nums, left, right, target, results):
    while left < right:
        if nums[left] + nums[right] == target:
            # we found 2 numbers here
            results.append([-target, nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                # if current num is same as before, jump it
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                # if current num is same as before, jump it
                right -= 1
        elif nums[left] + nums[right] > target:
            # move right
            right -= 1
        else:
            #move left
            left += 1


if __name__ == '__main__':
    print(threeSum([1, 2, -3, 5, 3, -8, 10, -20, 10]))
