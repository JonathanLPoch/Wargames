# /r/lolphp

Looking at the site and the provided source, two values must be provided such that they are not equal (`==`), but they must be...equal (`===`). Their `sha256` hashes must be the same. It's not like there was a custom implementation of `sha256` to poke at, or a known collision like SHA1 we could leverage.

But, PHP has this property where an array, when converted to a string, is equal to the string `"Array"`. So this is all we need.

`http://offsec-chalbroker.osiris.cyber.nyu.edu:1245/?thing1[]=abc&thing2[]=def`

So for the first check, `"abc"` and `"def"` are not equal. But when hashing, the values are interpreted as strings, meaning the two values are `"Array"`. That's our collision!

Here's the flag:

`flag{/r/lolphp_1s_actua11y_a_g00d_r3s0urce_159a1d429c6a}`
