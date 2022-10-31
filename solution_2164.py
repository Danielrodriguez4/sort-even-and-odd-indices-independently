

class Solution(object):

    def sortEvenOdd(self, nums):
        self.particion(lambda i: i//2 if i %
                       2 == 0 else (len(nums)+1)//2+i//2, nums)
        nums[:(len(nums)+1)//2], nums[(len(nums)+1)//2:] = sorted(nums[:(len(nums)+1)//2]
                                                                  ), sorted(nums[(len(nums)+1)//2:], reverse=True)
        self.particion(lambda i: 2*i if i < (len(nums)+1) //
                       2 else 1+2*(i-(len(nums)+1)//2), nums)
        return nums

    def particion(self, index, nums):
        for i in range(len(nums)):
            j = i
            while nums[i] >= 0:
                j = index(j)
                nums[i], nums[j] = nums[j], ~nums[i]  # procesados
        for i in range(len(nums)):
            nums[i] = ~nums[i]  # restaura valores
