# logmein again

So this time, the site looks the same as the first `logmein` challenge. Trying the same queries that worked in the first challenge will still log you in, but obviously the flag was not there. The message says, it is somewhere else. The challenge clue mentione Equifax and dumping a database, and it looks like this is what we're going to have to do. But, we know nothing about the database we're working with.

We can use the `information_schema` schema of the database to pull specific tables and columns. I wrote a script (see `log_me_in_again.py`) to accomplish this. It first looks for the database/schema name, then it goes on to look at the table and column names. This is done by taking the respective name from `information_schema`, and checking each character. If the character matches, a login will occur, which is shown by an `HTTP 302` response. If not, there will be a `HTTP 200` response which is what results from a failed login. It has the potential to find all database schema, all tables, and all column/row values character by character.

The script could also be modified to force an  `HTTP 500` internal server error, if needed.

After running the script, we get the flag:
`flag{1_r3ally_d0nt_have_a_g00d_id3a_for_a_flag_cc30b023aa85}`

