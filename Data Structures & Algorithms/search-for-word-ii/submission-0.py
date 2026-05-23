class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # stores full word at terminal node
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1) Build trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            ch = board[r][c]

            # important: stop if this path is not a valid prefix
            if ch not in node.children:
                return
            nxt = node.children[ch]
            # found a complete word
            if nxt.word is not None:
                ans.append(nxt.word)
                nxt.word = None   # avoid duplicates

            # mark visited
            board[r][c] = "#"

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)

            # unmark
            board[r][c] = ch

        # 2) Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return ans