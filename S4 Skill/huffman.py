import heapq
import os
import pickle
import sys
from collections import defaultdict

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(input_file):
    freq = defaultdict(int)
    with open(input_file, 'rb') as f:
        byte = f.read(1)
        while byte:
            freq[byte] += 1
            byte = f.read(1)
    return freq

def build_huffman_tree(freq):
    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop two nodes with the lowest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new node with these two nodes as children
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the merged node back to the heap
        heapq.heappush(heap, merged)

    # The heap now contains only one element, the root of the Huffman tree
    return heap[0]

# Function to generate Huffman codes from the tree
def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Function to encode a file using Huffman coding
def encode_file(input_file, output_file):
    # Calculate frequency of each byte in the input file
    freq = calculate_frequency(input_file)

    # Build the Huffman tree
    root = build_huffman_tree(freq)

    # Generate Huffman codes
    huffman_codes = generate_huffman_codes(root)

    # Write the compressed file
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        # Save the Huffman tree for decompression
        pickle.dump(root, outfile)
        
        # Write the encoded bits
        bitstring = ""
        byte = infile.read(1)
        while byte:
            bitstring += huffman_codes[byte]
            byte = infile.read(1)

        # Padding to make the bitstring a multiple of 8
        padding = 8 - len(bitstring) % 8
        bitstring = f"{padding:08b}" + bitstring + "0" * padding

        # Convert bitstring to bytes and write to the output file
        for i in range(0, len(bitstring), 8):
            byte = bitstring[i:i + 8]
            outfile.write(bytes([int(byte, 2)]))

# Function to decode a file using Huffman coding
def decode_file(input_file, output_file):
    # Open the compressed file
    with open(input_file, 'rb') as infile:
        # Load the Huffman tree
        root = pickle.load(infile)

        # Read the padding information
        padding = bin(ord(infile.read(1)))[2:].zfill(8)

        # Read the encoded data
        bitstring = ""
        byte = infile.read(1)
        while byte:
            bitstring += f"{ord(byte):08b}"
            byte = infile.read(1)

        # Remove the padding from the bitstring
        bitstring = bitstring[:-padding]

        # Decode the bitstring using the Huffman tree
        current_node = root
        decoded_bytes = bytearray()
        for bit in bitstring:
            current_node = current_node.left if bit == '0' else current_node.right
            if current_node.char is not None:
                decoded_bytes.append(current_node.char)
                current_node = root

        # Write the decoded bytes to the output file
        with open(output_file, 'wb') as outfile:
            outfile.write(decoded_bytes)

# ----------- Main Program -----------

def main():
    # Check if the correct arguments are passed
    if len(sys.argv) < 4:
        print("Usage:")
        print("To compress: python huffman.py -c <input_file> <output_file>")
        print("To decompress: python huffman.py -d <input_file> <output_file>")
        sys.exit(1)

    # Get the operation type (compression or decompression)
    operation = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if operation == '-c':
        # Compression
        print(f"Compressing {input_file} to {output_file}...")
        encode_file(input_file, output_file)
        print("Compression complete.")
    
    elif operation == '-d':
        # Decompression
        print(f"Decompressing {input_file} to {output_file}...")
        decode_file(input_file, output_file)
        print("Decompression complete.")
    
    else:
        print("Invalid operation. Use -c for compression or -d for decompression.")
        sys.exit(1)

# Run the program
if __name__ == "__main__":
    main()
