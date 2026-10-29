class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()

            for col in range(9):
                digit = board[row][col]

                if digit == ".":
                    continue
                elif digit in seen:
                    return False
                else:
                    seen.add(digit)
        

        for col in range(9):
            seen = set()

            for row in range(9):
                digit = board[row][col]

                if digit == ".":
                    continue
                elif digit in seen:
                    return False
                else:
                    seen.add(digit)
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()

                for r in range(3):
                    for c in range(3):
                        digit = board[box_row + r][box_col + c]

                        if digit == ".":
                            continue
                        elif digit in seen:
                            return False
                        else:
                            seen.add(digit)

        return True
