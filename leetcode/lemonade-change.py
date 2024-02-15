class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 5,5,10,10,20
        #5,5,5,10,20
        # ^
        #{5:2,10:2,20:1}
        #20:{10,5},{5,5,5}
        #10:{5}
        #45,25,20
        #{5}
        #{}
        #{20}
        
        five = 0
        ten = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            if bills[i] == 10:
                ten += 1
                if five >= 1:
                    five -= 1
                else:
                    return False
            elif bills[i] == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                    continue
                elif five >= 3:
                    five -= 3
                    continue
                else:
                    return False
        return True