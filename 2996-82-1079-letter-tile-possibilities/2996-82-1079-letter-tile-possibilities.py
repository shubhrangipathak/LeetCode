class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        return self.backtrack(tiles, used)

    def backtrack(self, tiles, used):
        c = 0 
        for i in range(len(tiles)):
            if used[i] or (i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]):
                continue
                
            used[i] = True 
            c += 1 + self.backtrack(tiles, used)
            used[i] = False 
        return c