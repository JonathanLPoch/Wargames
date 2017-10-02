from pwn import *
from types import *

def setup():
  r.recvuntil(": ")
  r.sendline("jlp644")
  r.recvuntil("??\n")

def solveEquations():
  while True:
    line = r.recvline()
    if "flag" in line:
      print line
      return
    expression = line.split(" ")
    try: 
      lhs = int(expression[0], 0)
    except:
      expression[0] = wordsToNumber(expression[0])
      pass

    try: 
      rhs = int(expression[2], 0)
    except:
      expression[2] = wordsToNumber(expression[2])
      pass

    lhs = str(expression[0])
    op = str(expression[1])
    rhs = str(expression[2])

    r.sendline(str(eval(lhs + op + rhs)))
    r.recvline()

def wordsToNumber(wordString):
  numberDict = {
    "ZERO":"0",
    "ONE":"1",
    "TWO":"2",
    "THREE":"3",
    "FOUR":"4",
    "FIVE":"5",
    "SIX":"6",
    "SEVEN":"7",
    "EIGHT":"8",
    "NINE":"9",
  }
  numList = wordString.split("-")
  for k in range(0, len(numList)):
    numList[k] = numberDict[numList[k]]
  return ''.join(numList)
    
r = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1236)
setup()
solveEquations()
r.interactive()
