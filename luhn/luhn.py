
from string import capwords


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        nums = self.card_num
        try:
            nums = [int(num) for num in self.card_num.replace(' ','')]
            if len(nums) < 2:
                raise ValueError()
            if nums[0] == 0:
                nums.pop(0)
            for idx in range(len(nums)-2, -1, -2):
                nums[idx] *= 2
                if nums[idx] > 9:
                    nums[idx] -= 9
            if sum(nums) % 10 != 0:
                raise ValueError()

            return True
        except:
            return False
            

        

