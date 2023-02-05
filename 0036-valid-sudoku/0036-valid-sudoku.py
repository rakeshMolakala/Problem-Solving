class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        cubes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n==".":
                    continue
                if n in rows[r]:
                    return False
                else:
                    rows[r].add(n)
                
                if n in cols[c]:
                    return False
                else:
                    cols[c].add(n)
                
                r_temp = r//3
                c_temp = c//3
                if n in cubes[(r_temp,c_temp)]:
                    return False
                else:
                    cubes[(r_temp,c_temp)].add(n)
        return True
                