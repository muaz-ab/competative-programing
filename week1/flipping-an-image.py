class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # fo]r i in range(len(image)):
        #     image[i] = image[i][::-1
        
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        return image