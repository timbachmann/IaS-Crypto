#!/bin/python3

import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

block_size = 16
key = b'!pre-shared-key!'
iv = b'4758403254850293'

def write_decrypted(bytes, path):
    file = open(path, "wb")
    file.write(bytes)
    file.close()


def read_encrypted(path):
    file = open(path, "rb")
    bytes = file.read()
    file.close()
    return bytes


def main(args):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_encrypted_text = read_encrypted(args.input)
    padded_plain_text = cipher.decrypt(padded_encrypted_text)
    plain_text = unpad(padded_plain_text, block_size)
    write_decrypted(plain_text, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Alice-Bob Decryption')
    parser.add_argument('-i', '--input', type=str, help="Path to encrypted file", required=True)
    parser.add_argument('-o', '--output', type=str, help="Path of decrypted file (should not exist)", required=True)
    args = parser.parse_args()
    main(args)
