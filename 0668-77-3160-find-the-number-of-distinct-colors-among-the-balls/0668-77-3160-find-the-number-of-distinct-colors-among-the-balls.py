class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        map_ball = {}

        color_map = Counter()

        for ball, color in queries:
            if ball in map_ball:
                old_color = map_ball[ball]
                color_map[old_color] -= 1 
                if color_map[old_color] == 0:
                    del color_map[old_color]
            
            map_ball[ball] = color
            color_map[color] += 1 

            res.append(len(color_map))
        
        return res