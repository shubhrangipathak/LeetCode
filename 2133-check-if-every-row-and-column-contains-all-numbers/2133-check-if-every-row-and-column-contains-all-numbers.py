class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        def resetHashmap(hashMap: dict) -> dict:
            for index in range(1, len(hashMap) + 1):
                hashMap[index] = 0
            return hashMap
                
        length = len(matrix)
        hashMap = defaultdict(int)
        
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
                # numPresent = isPresent(l,matrix[i][j])
                # if numPresent == False:
                     # return False
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
    
    #Checking if number present
#         def isPresent(numList :List[int],num:int)->bool: 
#             for index in range(len(numList)):
#                 if numList[index]==num:
#                     return True
#             return False
            