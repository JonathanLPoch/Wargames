from pwn import *

def ten_to_base(n,base):
  convertString = "0123456789ABCDEF"
  if n < base:
    return convertString[n]
  else:
    return ten_to_base(n//base,base) + convertString[n%base]

def parse_line(line):
  arr = line.strip().split(" ")
  starting_base = arr[1].strip("[]")
  value = arr[3].strip("()")
  target_base = arr[6].strip("{}")
  r.sendline(ten_to_base(int(value, int(starting_base)), int(target_base)))

def solve_bases():
  while True:
    r.recvline()
    line = r.recvline()
    if "flag" in line:
      print line
      return
    parse_line(line)


r = remote("216.165.2.56", 9001)
solve_bases()
