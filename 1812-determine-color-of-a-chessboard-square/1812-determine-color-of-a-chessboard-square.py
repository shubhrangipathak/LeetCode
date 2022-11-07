class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        if d[coordinates[0]]%2==0 or int(coordinates[1])%2==0:
            if d[coordinates[0]]%2==0 and int(coordinates[1])%2==0:
                return False
            return True
        return False