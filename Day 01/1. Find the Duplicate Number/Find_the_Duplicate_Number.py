class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        # print(slow,fast)
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print(slow,fast)
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow