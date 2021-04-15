#!/bin/python3

"""
AEAD is a standard that deinesn how to encrypt and sign files/data. It Uses AES with CBC Method and 
HMAC Hash to sign the data. 

This script takes an input file, a header and an output path.
It encrypts and signs the input file and writes it to the output file/path.

use head -c 54 ursprungsbild.bmp > myheader.bmp to save header to seperate file.
Then Append encrypted/signed output to header: cat myoutputfile.bmp >> myheader.bmp
-> This is the complete resulted encrypted file
"""

import argparse
from aead import AEAD


def read_plain(path):
    file = open(path, "rb")
    bytes = file.read()
    file.close()
    return bytes


def write_encrypted(bytes, path):
    file = open(path, "wb")
    file.write(bytes)
    file.close()


def main(args):
    cipher = AEAD(AEAD.generate_key())

    plain_text = read_plain(args.input)
    header = read_plain(args.header)

    cipher_text = cipher.encrypt(plain_text, header)
    print(header)

    write_encrypted(cipher_text, args.output)

    # Uncomment to change header and test the validation of signature
    # header += b'AAA'

    print(header)
    # Comment In to test validation
    cipher.decrypt(cipher_text, header)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AEAD Encryption')
    parser.add_argument('-i', '--input', type=str, help="Path to plain file", required=True)
    parser.add_argument('-header', '--header', type=str, help="Path to header file", required=True)
    parser.add_argument('-o', '--output', type=str, help="Path of encrypted file (should not exist)")
    args = parser.parse_args()
    main(args)
