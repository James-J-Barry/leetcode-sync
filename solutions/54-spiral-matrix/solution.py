class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix[0])
        n = len(matrix)
        #swap these to troubleshoot
        i, j = 0, 0
        top, bottom, left, right = -1, n, -1, m

        result = []
        while True:
            #go right
            if j >= right:
                break
            while j < right:
                result.append(matrix[i][j])
                j += 1
            j -= 1
            top += 1
            #go down
            i += 1
            if i >= bottom:
                break
            while i < bottom:
                #print(result)
                result.append(matrix[i][j])
                i += 1
            right -= 1
            i -= 1
            #go left
            j -= 1
            if j <= left:
                break
            while j > left:
                result.append(matrix[i][j])
                j -= 1
            bottom -= 1
            j += 1
            #go up
            i -= 1
            if i <= top:
                break
            while i > top:
                result.append(matrix[i][j])
                i -= 1
            left +=1
            i += 1
            j += 1
        return result
            
        