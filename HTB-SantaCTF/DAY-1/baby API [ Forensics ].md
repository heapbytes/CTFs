# baby APT [ Forensics ]
![image](https://user-images.githubusercontent.com/56447720/144394496-6bd7e734-7488-44c4-9b68-ff0926e6996d.png)

## Note 

- This is unintended way to do the challenge

### Solution

- Strings command showed some HTTP requets

![image](https://user-images.githubusercontent.com/56447720/144395334-ba542eba-cf63-45a3-9f99-18cd6cff1875.png)

- URL encoded
```bash
cmd=rm++%2Fvar%2Fwww%2Fhtml%2Fsites%2Fdefault%2Ffiles%2F.ht.sqlite+%26%26+echo+SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59+%3E+%2Fdev%2Fnull+2%3E%261+%26%26+ls+-al++%2Fvar%2Fwww%2Fhtml%2Fsites%2Fdefault%2Ffiles

```
- URL decoded

```bash
cmd=rm  /var/www/html/sites/default/files/.ht.sqlite && echo SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59 > /dev/null 2>&1 && ls -al  /var/www/html/sites/default/files

```

### Flag

```bash
└─$ echo "SFRCezBrX24wd18zdjNyeTBuM19oNHNfdDBfZHIwcF8wZmZfdGgzaXJfbDN0dDNyc180dF90aDNfcDBzdF8wZmYxYzNfNGc0MW59" | base64 -d 

HTB{0k_n0w_3v3ry0n3_h4s_t0_dr0p_0ff_th3ir_l3tt3rs_4t_th3_p0st_0ff1c3_4g41n}

```

