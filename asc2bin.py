#!/usr/bin/python

# convert asccii hex string to binary data

# usage in terminal:
# echo 41414144 | python asc2bin.py
#     -> writes AAAD to stdout

# see file readme.md for more details

import os
import sys
import re
import binascii
from pathlib import Path


def read_file(file_name):
	input_file = Path(file_name)
	if not input_file.exists():
		raise FileNotFoundError("File doen't exist.")
	file_data = input_file.read_text()
	return file_data

def write_file(file_name, data):
	output_file = Path(file_name)
	output_file.write_bytes(data)

# begin main

# parse program arguments
args = sys.argv
input_file_name = ""
output_file_name = ""
if len(args) >= 2:
    input_file_name = args[1]
if len(args) >= 3:
    output_file_name = args[2]


if input_file_name:
	try:
		print(f"loading input file '{input_file_name}'")
		txtin = read_file(args[1])
		print("input data:")
		print(txtin)
	except Exception as e:
		print(f"Cannot read file '{args[1]}'.", e)
		exit(1)
else:
	print("input data:")
	txtin = sys.stdin.readline()
	print(txtin)

if not txtin:
	print("No input provided. Exiting.")
	exit(1)

txt_data = re.sub(r'[^a-zA-Z0-9]','', txtin)
#print("data:", txt_data)
try:
	bin_data = binascii.a2b_hex(txt_data)
	if output_file_name:
		# write to filename
		print(f"writing output file '{output_file_name}'")
		write_file(output_file_name, bin_data)
	else:
		# write to stdout
		sys.stdout.write(bin_data.decode('utf-8'))
except binascii.Incomplete as e:
	print("[+] Error: Incomplete input", e)
	exit(1)
except TypeError as e:
	print("[+] Type Error:", e)
	exit(1)
except binascii.Error as e:
	print("[+] Error: Odd number of characters supplied:", e)
	exit(1)
except Exception as e:
	print("[+] Error:", e)
	exit(1)
