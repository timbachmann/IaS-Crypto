#!/bin/python3

import argparse
from Crypto.Cipher import AES               # requires 'pycrypto' package
from Crypto.Util.Padding import pad, unpad  # requires 'pycrypto' package

block_size = 16            # Since aes is a block cipher, we need to define a block size
key = b'!pre-shared-key!'  # This is the preshared AES key
iv = b'4758403254850293'


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
    cipher = AES.new(key, AES.MODE_CBC, iv)

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
