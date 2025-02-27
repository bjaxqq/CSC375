# Lempel-Ziv-Welch Compression 

## Skill Description

S5. Implement an *efficient* solution to a computational problem using advanced data structures and advanced techniques.

## Assignment Instructions

Write a program that uses LZW compression to compress and decompress text. In this case, the text will just be the letters A,C,G,T. This is to simulate compressing and decompressing DNA information coded as a sequence of nucleotides.

For reference you can use our lesson recording and also check out the Wikipedia article on [LZW](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch).

Requirements:

1. It should support compression and (lossles) decompression using LZW technique.
2. It should only consider the letters ACGT.
3. For consistency in the encoding and decoding, initially you should start with the following values in your dictionary A=0, C=1, G=2, T=3.
4. It is not processing files but just input text. See the example run below.
5. Compressing:

    1. Input: The text to compress will just be a string of letters, onr line. E.g. ACGCGCGTACGCGTA
    2. Output: The index values for each compressed pattern found, as described in the article and discussed in class. These will be separated by spaces. E.g.: 0 1 2 5 5 3 4 6 2 9

6. Decompressing: (Essentially the reverse)

    1. Input: The index values for each compressed pattern separated by spaces. E.g: 0 1 2 5 5 3 4 6 2 9
    2. Output: The uncompressed text which should be a single line of letters. E.g: ACGCGCGTACGCGTA

Additional Notes:

1. You can either have two different programs - one for compression and one for decompression - or a single program that takes an argument (or asks for input) on deciding which operation to perform.
2. Include clear instructions (in the header comments of your code) on how to run the program to both compress and decompress.
3. You are **not** writing these at the **byte** level. It would be important for actual file compression/decompression but this is just to make it easier to test the LZW implementation.
4. Here is an example run:

    ```
    PS C:\Users\caduncan\Projects\LZW> python .\lzw.py
    C
    ACGCGCGTACGCGTA
    0 1 2 5 5 3 4 6 2 9
    PS C:\Users\caduncan\Projects\LZW> python .\lzw.py
    D
    0 1 2 5 5 3 4 6 2 9
    ACGCGCGTACGCGTA
    ```

5. As always you can work in groups of up to 5 people. To give credit to everyone on the team, be sure to include their names in the header comments of your file.
6. This is an S skill. It is not necessary to complete this to pass the class but it does raise your overall grade.