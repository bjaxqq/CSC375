class Solution:
    def min_distance(self, word1: str, word2: str) -> int:
        # Getting lengths of input strings
        m, n = len(word_1), len(word_2)

        # Creating dynamic programming table with m + 1 rows and n + 1 columns
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initializing the DP table
        # Deletion cost = 3, total cost = i * 3.
        for i in range(1, m + 1):
            dp[i][0] = i * 3

        # Insertion cost = 3, total cost = j * 3.
        for j in range(1, n + 1):
            dp[0][j] = j * 3

        # Filling in dynamic programming table
        # Iterating through characters of word_1 and word_2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current word_1 and word_2 characters matching no additional cost
                if word_1[i - 1] == word_2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If characters not matching find cost of each operation
                    # Replacing word_1[i-1] with word_2[j-1] for substitution, cost = 5.
                    sub_cost = dp[i - 1][j - 1] + 5

                    # Inserting word_2[j-1] to word_1 for insertion, cost = 3.
                    in_cost = dp[i][j - 1] + 3

                    # Delete word_1[i-1] from word_1 for deletion, cost = 3
                    del_cost = dp[i - 1][j] + 3

                    # Swap word_1[i-1] and word_1[i-2], matching word_2[j-1] and word_2[j-2]
                    # Only works if i > 1, j > 1; word_1[i-1] == word2[j-2]; word1[i-2] == word2[j-1], cost = 2
                    swap_cost = float('inf')
                    if i > 1 and j > 1 and word_1[i - 1] == word_2[j - 2] and word_1[i - 2] == word_2[j - 1]:
                        swap_cost = dp[i - 2][j - 2] + 2

                    # Choose minimum cost among substitution, insertion, deletion, swap
                    dp[i][j] = min(sub_cost, in_cost, del_cost, swap_cost)

        # Final answer = minimum cost to transform word_1 to word_2
        return dp[m][n]