class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        all_path = set()
        
        def backtracking(x,y,arr):
            if len(arr)<len(word) and "".join(arr)!=word[:len(arr)]:
                return False
            if len(arr)>len(word):
                return False
            if len(arr)==len(word):
                if "".join(arr)==word:
                    return True
                return False
            all_path.add((x,y))
            for xx,yy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=xx<=R-1 and 0<=yy<=C-1 and (xx,yy) not in all_path:
                    arr.append(board[xx][yy])
                    temp_path = backtracking(xx,yy,arr)
                    if temp_path:
                        return True
                    arr.pop()
                    if (xx,yy) in all_path:
                        all_path.remove((xx,yy))
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j]==word[0]:
                    all_path = set()
                    ans = backtracking(i,j,[board[i][j]])
                    if ans:
                        return True
        return False