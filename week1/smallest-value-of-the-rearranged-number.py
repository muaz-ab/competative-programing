class Solution:
    def smallestNumber(self, num: int) -> int:
        con = []
        for nums in str(num):
            con.append(nums)
                    
        if num < 0:
            con = con[1:]
            con.sort(reverse=True)
            result = ''.join(map(str, con))
            print(result)
            return int(result)*-1
               
            return int("".join(con))
        elif '0'  in str(num):
            con.sort()
            for i in range(len(con)):
                if int(con[i]) != 0:
                    con[0] , con[i] = con[i] , con[0]
                    break
            result = ''.join(con)
            return int(result)
        else:
            con.sort()
            result = ''.join(con)
            return int(result)
        
        