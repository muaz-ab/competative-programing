class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_min = y_min = -1
        x_max, y_max = len(matrix[0]), len(matrix)
        dx, dy = 1, 0
        posx = posy = 0
        result = []
        for _ in range(x_max*y_max):
            if posx < x_max and posx > x_min and posy < y_max and posy > y_min:
                result.append(matrix[posy][posx])
                posx += dx
                posy += dy
            else:
                if dx == 1 and dy == 0:
                    dx = 0
                    dy = 1
                    posx -= 1
                    posy += 1
                    result.append(matrix[posy][posx])
                    posx += dx
                    posy += dy
                    y_min += 1
                elif dx == 0 and dy == 1:
                    dx = -1
                    dy = 0
                    posx -= 1
                    posy -= 1
                    result.append(matrix[posy][posx])
                    posx += dx
                    posy += dy
                    x_max -= 1
                elif dx == -1 and dy == 0:
                    dx = 0
                    dy = -1
                    posx += 1
                    posy -= 1
                    result.append(matrix[posy][posx])
                    posx += dx
                    posy += dy
                    y_max -= 1
                else:
                    dx = 1
                    dy = 0
                    posx += 1
                    posy += 1
                    result.append(matrix[posy][posx])
                    posx += dx
                    posy += dy
                    x_min += 1
        return result