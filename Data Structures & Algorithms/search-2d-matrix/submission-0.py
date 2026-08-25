class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l,r = 0 , len(matrix[0]) - 1
            if target >= matrix[i][l] and target <= matrix[i][r]:
                while l <= r:
                    mid = (r - l)//2
                    if matrix[i][l] == target:
                        return True
                    elif matrix[i][r] == target:
                        return True                
                    elif target > mid:
                        l = mid + 1
                        r = r - 1
                    elif target < mid:
                        l+=1
                        r = mid - 1
                    else: 
                        return True
        return False