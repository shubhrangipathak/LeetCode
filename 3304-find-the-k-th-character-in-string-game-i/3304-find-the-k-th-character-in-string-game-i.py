class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
    
        while len(word) < k:
            next_word = ""
            for char in word:
                if char == 'z':
                    next_char = 'a'
                else:
                    next_char = chr(ord(char) + 1)
                next_word += next_char

            word += next_word

        return word[k - 1]  