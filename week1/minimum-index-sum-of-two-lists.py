class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        Map = {}
        for i in range(len(list1)):
            Map[list1[i]] = i
        mini = float('inf')
        for j in range(len(list2)):
            if list2[j] in Map:
                sum_l = j + Map[list2[j]]
                if sum_l < mini:
                    mini = sum_l
                    result = []
                    result.append(list2[j])
                elif sum_l == mini:
                    result.append(list2[j])
        return result