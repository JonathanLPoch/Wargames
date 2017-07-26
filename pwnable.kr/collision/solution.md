# Collision

So this problem requires a password. In examining the main function I see that the passcode has 2 requirements:

`if(strlen(argv[1]) != 20)`
`if(hashcode == check_password( argv[1] ))`

It has to be 20 characters long (1 char = 1 byte in C), and it has to equal a `hashcode` constant that was set to `0x21DD09EC`. We can see that our input goes through a function called `check_password`.

Essentially, `check_password` iterates through the password and finds the sum of the 20 bytes. This is done by iterating through each set of 4 bytes (5 iterations) and adding the sum as an integer (1 int = 4 bytes). That sum must be equal to `0x21DD09EC`. So to find the correct passcode, we convert `0x21DD09EC` to an integer, which is `568134124`, and divide it by 5. We find that the result is `113626824.8`. In converting that number to hexadecimal, and using little endian (intel), we have the following input as our solution:

`./col $(perl -e 'print "\xC9\xCE\xC5\x06" x 4 . "\xC8\xCE\xC5\x06"')`

