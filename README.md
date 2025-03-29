asc2bin
=======

# Summary

Convert ASCII codes into a binary file via the command line.

Requires Python3 to run:\
https://www.python.org/

# Usage
### Run with Python
```shell
echo 41424344 | python asc2bin.py 
ABCD
```

or
```shell
python asc2bin.py input.txt output.bin
```
-> reaad file input.txt and writes result to file output.bin

or
```shell
python asc2bin.py input.txt
```
-> reads file input.txt and writes result to stdout

or
```shell
python asc2bin.py
```
-> reads from stdin and writes to stdout

### Run via shell script
Windows:
```shell
asc2bin.bat input.txt output.bin
```

Linux:
```shell
./asc2bin.sh input.txt output.bin
```
