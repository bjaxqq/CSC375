def find_lcs(string_1, string_2, string_3):
    # Getting lengths of the input strings
    a, b, c = len(string_1), len(string_2), len(string_3)

    # Creating a table to store lengths of the LCS
    # +1 is when one or more strings are empty
    table = [[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]

    # Filling in the table
    # Iterating through each character of the strings
    for i in range(1, a + 1):  # Looping through first string
        for j in range(1, b + 1):  # Looping through second string
            for k in range(1, c + 1):  # Looping through third string
                # Checking if current characters of all strings match
                if string_1[i - 1] == string_2[j - 1] == string_3[k - 1]:
                    # Increasing LCS length by 1 compared to LCS of previous characters if a match
                    table[i][j][k] = table[i - 1][j - 1][k - 1] + 1
                else:
                    # LCS length maximum of the possible LCS lengths if no match
                    # Excluding current characters of all strings
                    table[i][j][k] = max(table[i - 1][j][k], table[i][j - 1][k], table[i][j][k - 1])

    # Rebuilding LCS from table
    lcs = []  # Storing LCS characters in reverse order.
    i, j, k = a, b, c  # Starting from end of all strings

    # Traversing table backwards to find LCS
    while i > 0 and j > 0 and k > 0:
        if string_1[i - 1] == string_2[j - 1] == string_3[k - 1]:
            # Characters are part of LCS if they match
            lcs.append(string_1[i - 1])  # Adding character to LCS
            i -= 1  # Moving to previous character in first string
            j -= 1  # Moving to previous character in second string
            k -= 1  # Moving to previous character in third string
        else:
            # Moving in direction of larger LCS table value if no match
            if table[i - 1][j][k] >= table[i][j - 1][k] and table[i - 1][j][k] >= table[i][j][k - 1]:
                i -= 1  # Moving to previous character in first string
            elif table[i][j - 1][k] >= table[i - 1][j][k] and table[i][j - 1][k] >= table[i][j][k - 1]:
                j -= 1  # Moving to previous character in second string
            else:
                k -= 1  # Moving to previous character in third string

    # Reversing LCS to get correct sequence
    lcs.reverse()
    # Converting list of characters to single string and returning
    return ''.join(lcs)


def main():
    import sys

    # Checking for correct number of CLI arguments
    if len(sys.argv) != 4:
        print("Usage: python lcs.py <string1> <string2> <string3>")
        return

    # Getting input strings from CLI arguments
    string_1 = sys.argv[1]
    string_2 = sys.argv[2]
    string_3 = sys.argv[3]

    # Finding LCS of strings
    lcs = find_lcs(string_1, string_2, string_3)

    # Printing LCS and length
    print(f"Longest common subsequence: {lcs}")
    print(f"Longest common subsequence length: {len(lcs)}")


if __name__ == "__main__":
    main()