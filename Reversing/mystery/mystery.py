import re

password = raw_input("What is the password?: ")

if not re.match(r'^([a-z0-9\_\:])+$', password):
    print "[Failed Check 1]\n"
    exit(-1)

appa = [[ord(c) for c in x] for x in password.split(":")]

if len(appa) != 3:#word1:word2:word3
    print "[Failed Check 2]\n"
    exit(-1)

if appa[0][::-1] != appa[0]:#first has to be palindrome
    print "[Failed Check 3]\n"
    exit(-1)

sorted_part = sorted(appa[1])
if sorted_part != [95, 95, 100, 100, 101, 101, 109, 110, 111, 111, 115, 117, 121]:#second word has to have these chars: _ _ d d e e m n o o s u y
    print "[Failed Check 4]\n"
    exit(-1)

if appa[2][0] - appa[2][7] != -2 \
    or appa[2][1] ^ appa[2][6] != 0 \
        or appa[2][2] * appa[2][5] != 9797 \
        or appa[2][3] + appa[2][4] != 198 \
        or appa[2][4] % appa[2][3] != 98 \
        or appa[2][5] + appa[2][2] != 198 \
        or appa[2][6] * appa[2][1] != 10201 \
        or appa[2][7] ^ appa[2][0] != 2:
    print "[Failed Check 5]\n"
    exit(-1)

print "Successfully passed every check!\n"
#! ! ! ! ! ! ! !
#0 e e d b a e 2

#Index
#0 1 2 3 4 5 6 7

# abba:__ddeemnoosuy:0eedbae2
