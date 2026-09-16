class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]

        boxes = {}

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                num = board[r][c]
                box = (r//3, c//3)

                if box not in boxes:
                    boxes[box] = set()
                
                if num in rows[r] or num in cols[c] or num in boxes[box]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True