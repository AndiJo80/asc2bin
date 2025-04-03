#!/usr/bin/python

# convert ascii hex codes to ascii characters

# usage in terminal:
# echo 41424144 | python hex2asc.py
#     -> writes ABAD to stdout

# see file readme.md for more details

import sys
import re
import binascii
from pathlib import Path


def read_file(file_name):
	input_file = Path(file_name)
	if not input_file.exists():
		raise FileNotFoundError("File doesn't exist.")
	file_data = input_file.read_text()
	return file_data

def write_file(file_name, data):
	output_file = Path(file_name)
	output_file.write_bytes(data)

def run(args):
	# parse program arguments
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
		txtin = txtin.rstrip("\n") # remove trailing newline
		print(txtin)

	print() # print empty line for better readability
	if not txtin:
		print("No input provided. Exiting.")
		exit(1)

	hex_data = re.sub(r'[^a-zA-Z0-9]','', txtin)
	#print("data:", hex_data)
	try:
		bin_data = binascii.a2b_hex(hex_data)
		if output_file_name:
			# write to filename
			print(f"writing output file '{output_file_name}'")
			write_file(output_file_name, bin_data) # write as ascii text
		else:
			# write to stdout
			sys.stdout.write(bin_data.decode('utf-8')) # write as ascii text
			sys.stdout.flush()
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

# ----------- begin main ------------------
if __name__ == "__main__":
    run(sys.argv)
else:
	print("This script is not intended to be imported as a module.")
	print("Please run it directly from the command line.")
# ----------- end main --------------------