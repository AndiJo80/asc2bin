asc2bin
=======

# Summary

Convert hex codes into ascii characters (and back) via the command line.

Requires Python3 to run:\
https://www.python.org/

hex2asc.py - convert ascii hex codes to characters\
asc2hex.py - convert characters to ascii hex codes

# Usage
Both programs, *hex2asc* and *asc2hex*, are both used in very similar ways. They supports different cases:
- without input and output to console (stdout)
- with input from console (stdin) and output to console (stdout)
- with input from file and output to console (stdout)
- with input from file and output to file

### Run with Python
```shell
echo 41424344 | python hex2asc.py 
ABCD
```

or
```shell
python hex2asc.py input.txt output.bin
```
-> reaad file input.txt and writes result to file output.bin

or
```shell
python hex2asc.py input.txt
```
-> reads file input.txt and writes result to stdout

or
```shell
python hex2asc.py
```
-> reads from stdin and writes to stdout

### Run via shell script
Windows:
```shell
hex2asc.bat input.txt output.bin
```

Linux:
```shell
./hex2asc.sh input.txt output.bin
```
