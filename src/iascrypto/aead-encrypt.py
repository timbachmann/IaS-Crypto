#!/bin/python3

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

    #write_encrypted(cipher_text, args.output)

    header.replace(b'\x00', b'\x01')

    print(header)
    cipher.decrypt(cipher_text, header)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AEAD Encryption')
    parser.add_argument('-i', '--input', type=str, help="Path to plain file", required=True)
    parser.add_argument('-header', '--header', type=str, help="Path to header file", required=True)
    parser.add_argument('-o', '--output', type=str, help="Path of encrypted file (should not exist)", required=True)
    args = parser.parse_args()
    main(args)
