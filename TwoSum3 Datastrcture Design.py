#优化add
class TwoSum:
    nums = []

    def add(self, number):  # O(1)
        self.nums.append(number)

    def find(self, value):  # O(nlogn)
        self.nums.sort()  # O(nlogn)
        l, r = 0, len(self.nums) - 1
        while r != l:  # O(n)
            temp = self.nums[l] + self.nums[r]
            if temp == value:
                return True
            elif temp < value:
                l += 1
            else:
                r -= 1
        return False

    