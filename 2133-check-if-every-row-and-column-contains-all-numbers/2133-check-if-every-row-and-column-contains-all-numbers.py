class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        length = len(matrix)
        indexes = range(length)
        
        for i in indexes:
            if (len(set(matrix[i])) != length):
                return False
        
        
        for i in indexes:
            col = [matrix[j][i] for j in indexes]
            if (len(set(col)) != length):
                return False
                
        return True

    
    def checkValidInt(self, matrix: List[List[int]]) -> bool:

        def resetHashmap(hashMap: dict) -> dict:
            for index in range(1, len(hashMap) + 1):
                hashMap[index] = 0
            return hashMap
                
        length = len(matrix)
        hashMap = defaultdict(int)
        
        # initialising Dictionary to find the dupliczte 
        for index in range(1, length+1):
            hashMap[index] = 0

        # iterating by row 
        for i in range(len(matrix)):
            hashMap = resetHashmap(hashMap)
            for j in range(len(matrix[i])):
                number = matrix[i][j]
                if hashMap[number] == 0 :
                     hashMap[number] += 1 
                else :
                    return False

        # iterating by column
        for i in range(len(matrix)):
            hashMap = resetHashmap(hashMap)
            for j in range(len(matrix[i])):
                number = matrix[j][i]
                if hashMap[number] == 0 :
                     hashMap[number] += 1 
                else :
                    return False   
        return True
