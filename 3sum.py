
class Solution:

    def threeSum(self, nums):
        if(len(nums) < 3):
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[0:-2]):
            if i > 0 and v == nums[i-1]:
                continue
            tmp = {}
            for k in nums[i+1:]:
                if k not in tmp:
                    tmp[-v-k] = 1
                else:
                    res.add((v, -v-k, k))
        return list(res)


data = (-1, 0, 1, 2, -1, -4)
data1 = data[2:4]
data2 = data[2:4]
if data1 == data2:
    print("in it")
else:
    print("not in")
