#!/bin/python3

"""
This Version of the Script is more secure since the old MODE_EBC enrypts every block independantly what is
very insecure since one can easily find weaknesses like similarities in blocks to crack the encr.

This Version with Mode_CBC XOR a block with the encrypted previous one before encryption. This is more secure
since simple exploit of similarities and blocksize are not possible anymore. But Thjere is an Initialisation vector neccessary which must
be the same size as a block. This Vecor is XOR'd with the first block to encrypt.
"""

import argparse
from Crypto.Cipher import AES               # requires 'pycrypto' package
from Crypto.Util.Padding import pad, unpad  # requires 'pycrypto' package

block_size = 16            # Since aes is a block cipher, we need to define a block size
key = b'!pre-shared-key!'  # This is the preshared AES key 


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
    # Here a new aes encryptor is created
    cipher = AES.new(key, AES.MODE_ECB)

    # The Plain Text(message) is read from the inputfile and padded (filled up till right block size)
    plain_text = read_plain(args.input)
    padded_plain_text = pad(plain_text, block_size)

    # The message is ecrypted and saved to the outputfile
    cipher_text = cipher.encrypt(padded_plain_text)
    write_encrypted(cipher_text, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Alice-Bob Encryption')
    parser.add_argument('-i', '--input', type=str, help="Path to plain file", required=True)
    parser.add_argument('-o', '--output', type=str, help="Path of encrypted file (should not exist)", required=True)
    args = parser.parse_args()
    main(args)
