class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # Base case: if there's only one person, they are the winner (0-indexed)
        for i in range(2, n + 1):
            winner = (winner + k) % i

        return winner + 1