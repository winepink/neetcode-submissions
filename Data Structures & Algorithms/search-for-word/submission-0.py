class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r: int, c: int, idx: int) -> bool:
            # matched all characters
            if idx == len(word):
                return True

            # invalid cell or wrong character
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]
            ):
                return False
            # mark current cell as used
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # undo mark for other paths
            board[r][c] = temp

            return found
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
