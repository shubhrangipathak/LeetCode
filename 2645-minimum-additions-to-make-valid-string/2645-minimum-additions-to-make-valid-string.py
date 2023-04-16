class Solution:
    def addMinimum(self, word: str) -> int:
        
        if len(word) == 0:
            return 0 
        
        expected = 'a'
        count = 0
        i = 0 
        
        while i < len(word):
            curr = word[i]
            
            if expected == 'a':
                if curr != 'a':
                    count+=1
                    
                else:
                    i += 1
                expected = 'b'
                
            elif expected == 'b':
                if curr != 'b':
                    count += 1 
                else:
                    i += 1 
                expected = 'c'
                
            elif expected == 'c':
                if curr != 'c':
                    count += 1 
                else:
                    i += 1
                expected = 'a'
                
        if curr == 'a':
            count += 2 
        elif curr == 'b':
            count += 1 
            
        return count
       