# bof

Given bof.c, it looks like the function `func` is comparing the argument string `key` (in this case, `0xdeadbeef`) to the value `0xcafebabe`. The user input that the function asks for is stored in the string `overflowme` which is a char array of length 32. The only way to overwrite `key` is through a buffer overflow.

Through running a quick [checksec](https://github.com/slimm609/checksec.sh), we see that there is a stack canary enabled. Normally this would be problematic to trying to overflow the stack, but in this case it isn't really a problem.

First we run the program with an input of 32 "A"'s. When we examine the stack in `pwndbg`, we see our input: 

![stack](https://github.com/JonathanLPoch/Wargames-CTFs/blob/master/pwnable.kr/bof/img/stack.png)


Here we can see the layout of the stack relatively easily. The `0x41` is the hex representation of the ascii "A", and we can see where the variable overflowme lies. Right after this, we see the stack canary `0x3a5c9600`. We can print out the value of `$ebp`, the base pointer, and see that it is `0xffffcc98`. This means the address directly after it is the return address, `0x565569f`, and then we see the parameter `0xdeadbeef` passed into `func`.

With the size of the char array, the stack canary, the base pointer, and return address, we know we need to feed our buffer `52` characters in order to reach our parameter. After this, we will be directly overwriting the argument to function, `key`.

Since the program was compiled on a an x86 Linux system we already know it's a little endian system. So, our payload looks something like `"A"*52+"\xBE\xBA\xFE\xCA\x00"`. And from here, we simply `cat flag` from our shell.
