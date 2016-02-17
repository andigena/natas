This repo contains solutions and short descriptions for level 11-27 of [OverTheWire/Natas](http://overthewire.org/wargames/natas/). 
Probably the most interesting file is `natas16.py`.

## natas11

A **xor-encrypted** cookie with know plaintext and output. Calculating the key and forging a cookie with showpassword=yes gets us in.

## natas12

Upload a .php file instead of a JPEG and get the flag.
  
## natas13

Tries to validate the uploaded image with `exif_imagetype`,  which only checks the  signature at the start of the file, prefix the php payload with valid image header and it's business as usual.

## natas14

Textbook sql injection solvable with some 'or 1=1 # '. 

## natas15

Blind sqli, `./sqlmap.py --auth-type=basic --auth-cred=natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J -u http://natas15.natas.labs.overthewire.org/index.php --data="username=a" -p username --string=doesn --level=5 --user-agent=Mozilla --dbms=MySQL --threads 4 -D natas15 -T users --dump`

## natas16

Command injection in the vein of natas09 and natas10 but with more filtering:  

```
if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
```

We can execute commands via `$()` but I found no direct way to get their output. Instead, we can use it to brute-force the password char-by-char, by submitting something like: `$(grep -E ^a.* /etc/natas_webpass/natas17)zucchini`.

* if the first char of the password is 'a', we will receive an empty output of the outer grep since itt will search for `` `password`zucchini ``, which is not in dictionary.txt
* if the first char of the pass is not 'a', then the response will contain zucchini

The exploit implements both a linear and a binary search strategy.

## natas17

Time-based sqli, `./sqlmap.py --auth-type=basic --auth-cred=natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw -u http://natas17.natas.labs.overthewire.org/index.php --data="username=a" -p username --level=5 --user-agent=Mozilla --dbms=MySQL --threads 4 -D natas17 -T users --dump`

## natas18

Custom session handling with 640 possible session ids. Going through all of them will get us in.

## natas19

Based on natas18. Examining the cookie set upon login, it can be seen that it is hex encoded, decoding shows session ids of the following format: 45-admin. Just as previously, run through the possible session ids and send them in the right format.

## natas20

Custom session data serialization code enables us to inject session variables via `\n`.

## natas21

Co-located sites may share php sessions.

## natas22

If there is a key named `revelio` in the request then reveals the password but also uses `header("Location: /");` to redirect us before that happens. Ignore the redirect. 

## natas23

Emphasizes the nice type coercion rules of php, the password has to contain the string `iloveyou` and has to compare greater than the integer 10. Submitting `16iloveyou` gets us in.

## natas24

More type niceness, does `strcmp` on user-input to check a password. An array compares equal to a string.

## natas25

LFI after weak filtering of directory traversal payload. Another filter prevents us from directly including `/etc/natas_webpass/natas26`. We can put the php payload in the user-agent and include the logfile.

## natas26

Unserializes user-input. The payload can be created by copy-pasting the Logger class and writing out a serialized version initialized with proper values, e.g. `logFile = 'img/a.php'`, `exitMsg = <?php include("/etc/natas_webpass/natas27")?>`.

## natas27

MySQL string truncation and string comparison peculiarities. Had to cheat for this one to be honest.
