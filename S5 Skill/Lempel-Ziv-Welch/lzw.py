"""
Instructions:
1. Run the program
2. Choose either compression (C) or decompression (D)
3. Compression:
   - Input a DNA sequence (e.g. ACGCGCGTACGCGTA)
   - Output will be the compressed indices (e.g. 0 1 2 5 5 3 4 6 2 9)
4. Decompression:
   - Input the compressed indices (e.g. 0 1 2 5 5 3 4 6 2 9)
   - Output will be the decompressed DNA sequence (e.g. ACGCGCGTACGCGTA)

Author: Brooks Jackson
"""

def compress_lzw(input_text):
    # Initialize the dictionary with single-character patterns
    dictionary = {"A": 0, "C": 1, "G": 2, "T": 3}
    next_index = 4  # Next available index for new patterns
    current_pattern = ""
    compressed_indices = []

    for char in input_text:
        # Check if the current pattern + the new character exists in the dictionary
        combined_pattern = current_pattern + char
        if combined_pattern in dictionary:
            current_pattern = combined_pattern
        else:
            # Add the current pattern's index to the output
            compressed_indices.append(dictionary[current_pattern])
            # Add the new pattern to the dictionary
            dictionary[combined_pattern] = next_index
            next_index += 1
            # Start a new pattern with the current character
            current_pattern = char

    # Add the last pattern's index to the output
    if current_pattern:
        compressed_indices.append(dictionary[current_pattern])

    return compressed_indices

def decompress_lzw(compressed_indices):
    # Initialize the dictionary with single-character patterns
    dictionary = {0: "A", 1: "C", 2: "G", 3: "T"}
    next_index = 4  # Next available index for new patterns
    decompressed_text = ""

    # Get the first index and initialize the previous pattern
    previous_index = compressed_indices[0]
    decompressed_text += dictionary[previous_index]

    for current_index in compressed_indices[1:]:
        if current_index in dictionary:
            # If the current index is in the dictionary, add its pattern to the output
            current_pattern = dictionary[current_index]
            decompressed_text += current_pattern
            # Add the new pattern to the dictionary
            new_pattern = dictionary[previous_index] + current_pattern[0]
            dictionary[next_index] = new_pattern
            next_index += 1
        else:
            # Handle the special case where the index is not in the dictionary
            new_pattern = dictionary[previous_index] + dictionary[previous_index][0]
            decompressed_text += new_pattern
            dictionary[next_index] = new_pattern
            next_index += 1
        previous_index = current_index

    return decompressed_text

def main():
    print("LZW Compression and Decompression for DNA Sequences (A, C, G, T)")
    print("Enter 'C' for compression or 'D' for decompression:")
    mode = input().strip().upper()

    if mode == "C":
        print("Enter the DNA sequence to compress (e.g. ACGCGCGTACGCGTA):")
        input_text = input().strip().upper()
        if all(char in "ACGT" for char in input_text):
            compressed_indices = compress_lzw(input_text)
            print("Compressed indices:")
            print(" ".join(map(str, compressed_indices)))
        else:
            print("Error: Input must only contain A, C, G, or T.")
    elif mode == "D":
        print("Enter the compressed indices (e.g. 0 1 2 5 5 3 4 6 2 9):")
        compressed_indices = list(map(int, input().strip().split()))
        decompressed_text = decompress_lzw(compressed_indices)
        print("Decompressed DNA sequence:")
        print(decompressed_text)
    else:
        print("Error: Invalid mode. Please enter 'C' or 'D'.")

if __name__ == "__main__":
    main()