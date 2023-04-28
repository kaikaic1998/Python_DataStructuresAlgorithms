class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            if i == 0:
                lst = [[1]]
            elif i == 1:
                lst.append([1,1])
            else:
                row = []
                for j in range(0, i+1):
                    if j == 0 or j == i:
                        row.append(1)
                    else:
                        row.append( lst[i-1][j-1] + lst[i-1][j] )
                lst.append(row)
        return lst
