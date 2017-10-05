f = open('license', 'r')
line = f.readline()
print ":".join("{:02x}".format(ord(c)) for c in line)
