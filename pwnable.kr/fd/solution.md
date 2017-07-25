# fd
This was an exercise on file descriptors. The program asks for an integer, and subtracts 0x1234 from it:

`int fd = atoi( argv[1] ) - 0x1234;`

Linux file descriptors define `STDIN` as `0`, `STDOUT` as `1`, and `STDERR` as `2`. Since fd is an integer, the input value is subtracted by the integer equivalent, of 4660. The following line, `len = read(fd, buf, 32);` gives us the hint that we want `STDIN`, or `0` for `fd`. 

Then, the comparison:

`if(!strcmp("LETMEWIN\n", buf){`

...tells us that buf needs to be `LETMEWIN`. And so we have our solution:
`./fd 4660`
`LETMEWIN`
