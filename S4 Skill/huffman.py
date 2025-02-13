import heapq
import os
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(file_path):
    with open(file_path, "rb") as file:
        data = file.read()

    return Counter(data)

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(char=char, freq=freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)

def build_codebook(root, code="", codebook=None):
    if codebook is None:
        codebook = {}

    if root is not None:
        if root.char is not None:
            codebook[root.char] = code
        build_codebook(root.left, code + "0", codebook)
        build_codebook(root.right, code + "1", codebook)

    return codebook

def encode_file(input_file, codebook):
    encoded_bits = ""

    with open(input_file, "rb") as file:
        data = file.read()
        for byte in data:
            encoded_bits += codebook[byte]

    return encoded_bits

def write_compressed_file(output_file, codebook, encoded_bits):
    with open(output_file, "wb") as file:
        codebook_str = str(codebook)
        file.write(len(codebook_str).to_bytes(4, byteorder="big"))
        file.write(codebook_str.encode())

        padding = 8 - (len(encoded_bits) % 8)
        encoded_bits += "0" * padding
        file.write(padding.to_bytes(1, byteorder="big"))

        for i in range(0, len(encoded_bits), 8):
            byte = encoded_bits[i:i+8]
            file.write(int(byte, 2).to_bytes(1, byteorder="big"))

def compress_file(input_file, output_file):
    print(f"Compressing {input_file} to {output_file}...")

    freq_table = build_frequency_table(input_file)
    huffman_tree = build_huffman_tree(freq_table)
    codebook = build_codebook(huffman_tree)
    encoded_bits = encode_file(input_file, codebook)
    write_compressed_file(output_file, codebook, encoded_bits)

    print("Compression complete.\n")

def read_compressed_file(input_file):
    with open(input_file, "rb") as file:
        codebook_size = int.from_bytes(file.read(4), byteorder="big")
        codebook_str = file.read(codebook_size).decode()
        codebook = eval(codebook_str)
        padding = int.from_bytes(file.read(1), byteorder="big")
        encoded_bits = ""

        while byte := file.read(1):
            encoded_bits += f"{int.from_bytes(byte, byteorder='big'):08b}"

        encoded_bits = encoded_bits[:-padding]
    return codebook, encoded_bits

def decode_file(encoded_bits, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_data = bytearray()

    for bit in encoded_bits:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data.append(reverse_codebook[current_code])
            current_code = ""

    return decoded_data

def write_decompressed_file(output_file, decoded_data):
    with open(output_file, "wb") as file:
        file.write(decoded_data)

def decompress_file(input_file, output_file):
    print(f"Decompressing {input_file} to {output_file}...")

    codebook, encoded_bits = read_compressed_file(input_file)
    decoded_data = decode_file(encoded_bits, codebook)
    write_decompressed_file(output_file, decoded_data)

    print("Decompression complete.\n")

def display_menu():
    print("=" * 40)
    print("Huffman Coding")
    print("=" * 40)
    print("1. Compression")
    print("2. Decompression")
    print("3. Exit")
    print("=" * 40)

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            input_file = input("File to compress: ")
            output_file = input("Compressed output file name: ")
            compress_file(input_file, output_file)
        elif choice == '2':
            input_file = input("File to decompress: ")
            output_file = input("Decompressed output file name: ")
            decompress_file(input_file, output_file)
        elif choice == '3':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()