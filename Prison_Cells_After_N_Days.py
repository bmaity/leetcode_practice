'''
Prison Cells After N Days

There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], n = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
Output: [0,0,1,1,1,1,1,0]

 

Constraints:

    cells.length == 8
    cells[i] is either 0 or 1.
    1 <= n <= 109

'''


class Solution:
    @staticmethod
    def isAdjacent(curNdx, array):
        left = curNdx - 1
        right = curNdx + 1

        if (array[left] == 0 and array[right] == 0) or (array[left] == 1 and array[right] == 1):
            return True
        else:
            return False

    def prisonAfterNDays(self, cells, n):
        dic = {}
        for times in range(15):
            tmp_array = [0] * len(cells)
            for i in range(len(cells)):
                if i == 0:
                    tmp_array[i] = 0
                elif i == len(cells) - 1:
                    tmp_array[i] = 0
                elif self.isAdjacent(i, cells):
                    tmp_array[i] = 1
                else:
                    tmp_array[i] = 0
            cells = tmp_array
            dic[times] = cells
        adr = n % 14 - 1
        if adr == -1:
            adr = 13
        return dic[adr]
    
