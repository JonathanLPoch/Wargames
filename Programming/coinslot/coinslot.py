import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.chal.csaw.io", 8000))
line = s.recv(1024).replace(b',',b'')

print(line)
while True:
    if b'\n' in line:
        print(line)
        firstLine = line.split(b'\n')
        if len(firstLine) == 3:
            givenAmount = float(firstLine[1][1:])
            line = firstLine[2].replace(b',', b'')

        else:
            givenAmount = float(firstLine[0][1:])
            line = firstLine[1].replace(b',', b'')

    else:
        print(b'The line is: ' + line)
        if b'$' in line:
            dollar = line.index(b'$')
            space = line.index(b' ', dollar)
            amount = int(line[dollar+1:space])
        elif b'c' in line:
            if b'half-dollars' in line:
                amount = float(0.50)
            if b'quarters' in line:
                amount = float(0.25)
            if b'dimes' in line:
                amount = float(0.10)
            if b'nickels' in line:
                amount = float(0.05)
            if b'pennies' in line:
                amount = float(0.01)
        print(b'The given amount is: ',givenAmount)
        print(b'The amount is: ', amount)
        if (givenAmount == 0.00):
            s.send(b'0\n')
            print("SENDINGx: 0")
        elif (givenAmount >= amount):
            s.send(str(int(givenAmount/amount)) + b'\n')
            print("SENDING:" + str(int(givenAmount/amount)) + b'\n')
            givenAmount -= round(amount * int(givenAmount/amount),2)
            givenAmount = round(givenAmount,2)
        else:
            s.send(b'0\n')
            print("SENDINGy: 0")
        line = s.recv(1024).replace(b',',b'')
        if not line:
            break

s.close()