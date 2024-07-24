class NumArray:

    def __init__(self, nums):
        self.nums = nums
        for i in range(1,len(self.nums)):
            self.nums[i] += self.nums[i-1]            

    def sumRange(self, left: int, right: int) -> int:
        tr = self.nums[right]
        if left!=0:
            tl = self.nums[left-1]
        else:
            tl = 0
        return tr-tl


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)