# S4 Skill

## Skill Description

S4. Develop a correct implementation of a given advanced data structure.

## Assignment Instructions

Write a program that uses Huffman coding to compress and decompress (text) files.

**Requirements:**

1. It should support compression and (lossless) decompression 
2. It should create and use Huffman trees by analyzing each (byte) character (0-255) - counting frequencies, merging, etc.
3. It should support reading in a file and writing to a separate file.
4. The compressed file should store the Huffman tree as part of its initial information - as that is necessary to support decompression.

**Additional Notes:**

1. You can either have two different programs - one for compression and one for decompression - or a single program that takes an argument (or asks for input) on deciding which operation to perform.
2. The file to (de)compress can be given as a command line argument or prompted by the user.
3. Include clear instructions (in the header comments of your code) on how to run the program to both compress and decompress.
4. Here is an example:

```
PROMPT> java Huffman -c example.txt example.hc

Creates a file called example.hc with is the compressed form of example.txt

PROMPT> java Huffman -d example.hc example2.txt

Creates a file called example2.txt that is the decompressed form of example.hc
The files example.txt and example2.txt should be 100% identical.
```

5. You can be flexible on how your interface works but ultimately it should support compression and decompression using Huffman coding.
6. As always you can work in groups of up to 6 people. To give credit to everyone on the team, be sure to include their names in the header comments of your file.
7. This is an S skill. It is not necessary to complete this to pass the class but it does raise your overall grade.