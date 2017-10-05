# logmein

This was an exercise in SQL injection. The website was a simple login form, and the goal was to login as `admin`.

I tried inputting a `'` in the `email` field first, then the `password`. From the results (a 500 error), the `email` field appeared to be vulnerable to SQL injection. For the most basic login, I assumed the query to be something like:

`SELECT * FROM USERS WHERE email='$email' AND password='$password'`

So, the injection query could look something like this:

`admin' -- -`

This changed the query to:

`SELECT * FROM USERS WHERE email='admin' -- -' AND password='$password'`


It was a simple matter of inspecting the `email` element and changing the value from `email` to `text` to remove the valid email checking. And it worked, so I know this was only checked client-side. And, it worked. Here's the flag:

`flag{w0w_such_1337_SQLi_caecd8cced13}`

I actually found my solution the first time around without changing the `email` property of the input box. This was my solution:

`admin'or'1'='1--@gmail.com`

...it qualified as a valid email and passed all the appropriate checks. What's interesting is that it turned the query into this:

`SELECT * FROM USERS WHERE email='admin'or'1'='1--@gmail.com' AND password='$password'`

AND is evaluated before OR, so this query works! And if emails were verified for form on the backend, it wouldn't matter~


