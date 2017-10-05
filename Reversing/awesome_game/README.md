# crackme

The first protection I found in this crackme was some sort of anti-debugging mechanism. I tried running the binary without any issues, but when I set a breakpoint in `license_check`, the program terminated with a message: `Cheater!`

Putting this binary in Binary Ninja reveals something interesting. In `main`, there's a loop that goes over each word of memory of `license_check`. This loop performs an `xor` on each word, and checks it with a valid signature at the end which is `0x8162036f`. This is to check for any breakpoints (`0xcc`) that have been placed in the `license_check` function. Not even conditional breakpoints seem to work since those seem to overwrite a byte anyway.

In `license_check`, this same loop also exists. The `valid_sig` ensures that no breakpoint can ever be placed in, and the presence of this loop in the license_check means you can't wait until you even step to the `license_check` function to set breakpoints as it checks the entire function again.

Trying to run the game without any license gives the `Cheater!` message as well.

It also looks like the `game` function was somehow hidden as a function. In IDA, I saw that it was in the `.text` section. Using both Binary Ninja and objdump, the function was there but there was no clear way to see how the program was calling it. It wasn't as simple as calling the function by name.

I suppose other binary protections include the presence of a stack canary, and the NX bit.
