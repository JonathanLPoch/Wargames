# Osiris Lab Hack Night Bomb

This is a writeup of the binary bomb from NYU Tandon's OSIRIS Lab. I was given the **bomb** as a 32-bit ELF executable. Running `file bomb` showed this, and that the binary was not stripped. I dumped the assembly using `objdump -D bomb > bombAssembly.txt`

Next I found the main function in the assembly. In here, there's something interesting:
`8048ba0:	e8 fd fb ff ff       	call   80487a2 <round1>`
`8048ba5:	e8 3f fc ff ff       	call   80487e9 <round2>`
`8048baa:	e8 c7 fc ff ff       	call   8048876 <round3>`
`8048baf:	e8 98 fd ff ff       	call   804894c <round4>`

It looks like the main function is calling four rounds or phases. The first thing I did was open up pwndbg and set a breakpoint at **round1**.


## Phase 1
In the first phase, since the binary isn't stripped I can easily see a call to a method called prime:

`80487cd:	e8 79 ff ff ff       	call   804874b <prime>`

I assume the input for this phase is just a prime number, and supplying one seems to work.

Solution: 7 (a prime #)

## Phase 2
For the second phase, things aren't as straightforward. There aren't any explicit function calls, so a little digging is needed. After the call to take a user input I see the following:

`8048823:	e8 48 fd ff ff       	call   8048570 <fgets@plt>`
`8048828:	8d 85 f4 fe ff ff    	lea    -0x10c(%ebp),%eax`
`804882e:	89 04 24             	mov    %eax,(%esp)`
`8048831:	e8 aa fd ff ff       	call   80485e0 <strlen@plt>`
`8048836:	83 f8 04             	cmp    $0x4,%eax`
`8048839:	74 05                	je     8048840 <round2+0x57>`
`804883b:	e8 ed fe ff ff       	call   804872d <explode>`

The input is placed at `-0x10c(%ebp)`, which can be verified by `x/10c $ebp-0x10c`. Using gdb, I can see that the program checks to make sure the input is of length 4. `strlen` does not count the null terminator, but it does record the newline character so the input must be of length 3 (e.g. "abc\n" for a count of 4).

The next set of instructions of interest are the following:

`8048840:	0f b6 95 f4 fe ff ff 	movzbl -0x10c(%ebp),%edx`
`8048847:	0f b6 85 f6 fe ff ff 	movzbl -0x10a(%ebp),%eax`
`804884e:	38 c2                	cmp    %al,%dl`
`8048850:	74 05                	je     8048857 <round2+0x6e>`
`8048852:	e8 d6 fe ff ff       	call   804872d <explode>`

Earlier I found that `-0x10c(%ebp)` contained the user's input. So `movzbl -0x10c(%ebp)` instruction takes the first letter of the input and puts it in `$edx`. Similarly, `movzbl -0x10a(%ebp)` takes the *third* (or last) letter and puts that value in `$eax`. `cmp    %al,%dl` then checks for the equality of the lower 8 bits of `$eax` and `$edx`. 

In other words, the input must be 3 characters long, with the first and last characters being identical.

Solution: lol

## Phase 3
In the third phase, I see something similar to the second phase:

`80488b0:	e8 bb fc ff ff       	call   8048570 <fgets@plt>`
`80488b5:	8d 85 f4 fe ff ff    	lea    -0x10c(%ebp),%eax`
`80488bb:	89 04 24             	mov    %eax,(%esp)`
`80488be:	e8 1d fd ff ff       	call   80485e0 <strlen@plt>`
`80488c3:	83 f8 07             	cmp    $0x7,%eax`

It looks like an input of length 6 is needed this time.

In the following series of instructions, the same set is repeated several times. Six, to be exact.

`80488cd:	0f b6 85 f4 fe ff ff 	movzbl -0x10c(%ebp),%eax`
`80488d4:	3c 6f                	cmp    $0x6f,%al`
`80488d6:	74 05                	je     80488dd <round3+0x67>`
`80488d8:	e8 50 fe ff ff       	call   804872d <explode>`

What's happening here is, since `-0x10c(%ebp)` contains the first character of the input string, that value is being moved to `$eax`, and it gets compared to the value `$0x6f`. This value happens to be the ascii value for 'o'. In looking at the following repetitions, the resulting string is 'osiris'.


Solution: osiris

## Phase 4

Solution: deadbeef

