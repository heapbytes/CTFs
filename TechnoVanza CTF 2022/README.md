
# Technovanza CTF Writeup

![image](https://user-images.githubusercontent.com/56447720/154837679-00b6ee27-272f-4d2d-a0d9-140524aedb17.png)


# Challenges

## D3vel0peR

### File

![maxresdefault](https://user-images.githubusercontent.com/56447720/154837720-03356c14-dc68-44c3-b9a9-beb0c04c48bc.jpg)

- Given was a image
- I tried many steg tools but found nothing intresting
- Read the description, said the web develope has somthing for you
- The flag was in source code of the website ``

### Flag

![image](https://user-images.githubusercontent.com/56447720/154837815-77f12ee5-22d7-4cce-81ba-092eb582857e.png)

```bash
flag : TECHNO(lOv3_T3chn0vANZa)
```

## Future

### File

![note (1)](https://user-images.githubusercontent.com/56447720/154838434-adb8b1d8-e653-4a59-8d4d-28b1c428ab98.png)

- It's a cipher
- `https://www.dcode.fr/futurama-alien-alphabet`

```bash
Flag :  TECHNO(we_are_not_alone)
```

## aquaman

### Description

```
It was a long time ago when Aquaman had a small feast, but his friends refused to agree. He lost the photo; his friends want him to tell the date and time of when they ate. Aquaman roughly remembers the month and year to be knjwamujkkvbivznqjmpeye can u help him find the complete date and time. Flag Format: TECHNO(yyyy-mm-dd_hh-mm-ss)
```

### SOlve

- See instagram
- They had lunch on sept 2018
- Used osintgram to find exact time

```bash
#flag : TECHNO(2018-09-27_19-14-46)
```

## can you find the difference?

### File

![vjti_pic](https://user-images.githubusercontent.com/56447720/154838800-b0313f5a-83fe-42d8-970d-8b8c0355bb09.jpg)

### SOlve

- Used strings to get the flag

![image](https://user-images.githubusercontent.com/56447720/154838829-8bb40af3-27e3-4ca3-a9e9-666ed9686ce5.png)

```bash
# Flag : TECHNO(vjti_campus_I5_b34u7iFul)

```

## Jumping Jack

- Was just bunch of base64 and base32 encrypted

### Solve

```bash
╰─ echo "KMYUURCWNRLFKUZRMRHVI23YI5JTCWSUKJVXAS2SGBKTAVLLJZGFIRKKJRJGWMKYKUYDKS2WNRNFSU2WJZKFI2ZVKNKGWVS2KZVU4V2UGBFE6UTLNN4U22SKJNIWW6CIKZ5FMRCVKV2FGUSFLJDFK6SKKRKGYSSLKJVXIVKUIUYUUU3LLJDVCVSWJNHFK2CWKBKDAOKQKQYDS===" | base32 -d | base64 -d | base32 -d | base64 -d | base32 -d | base64 -d
adMin_S4yS_"1Ol"
```

```bash
# Flag : TECHNO(adMin_S4yS_"1Ol")
```

## malwar3

- Given was a `.docx` file
- After i opened it.... it had `PK` which is initial bytes used to describe `.zip` files
- Rename

```bash
└─$ mv malwar3.docx mal.zip

##########################

└─$ unzip mal.zip
Archive:  mal.zip
  inflating: [Content_Types].xml
  inflating: documentProps/app.xml
  inflating: documentProps/core.xml
   creating: word/_rels/
  inflating: word/_rels/document.xml.rels
  inflating: word/file.xml
  inflating: word/font.xml
  inflating: word/settings.xml
  inflating: word/styleSettings.xml
   creating: word/theme/
  inflating: word/theme/theme1.xml
  inflating: word/webSettings.xml

```
### SOlve

- Last line of `word/file.xml` had some characters
- `<,s[-1i?Yl:24?-<+SG-->`
- It was encoded with `Ascii85`

- Flag

```bas
# TECHNO(Tr0j4n_INjeCTeD)
```


## landlord why u like dis?

- Extract all the flies using : `sudo unsquashfs -f -d <directory-you-want-to-extract> <filename>`

- Find key and cipher text
- Cipher text
```bash
    ╰─$ cat ciphertxt.enc
OuWrlAKbKZjfRw11VWv81kq40ZHemgJKR39be3vVn9JodbKTGczpZPITPLWAJvDrv96rq46/BnPgY/+3S0SlbRUWFBZvsxwk6FcEKwsyT+Kr/0ng5Jx0sPKkMqSgHisTzyZoCUv3pfUYP587TXBaQz2MSSNIxWJ4fUkbjlbKXas=
{but where is the key?}
```

- Private key

```bash
 ╰─$ cat private.key
-----prIv473_Key-----
MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBALtdcbD3walQVFxgTd8uAxgVarRPtgTHTI7CDnAHVUvvYzDRyZcE31vagVG3StncJiqc8Nv2yTYRTh5qFLg3192BL3W5vo6Qc7DqHQxja+/21sAnbpQng7zc9yvH4fh6LLQA/rDS14hrk01PJH96S+cghlbYXPqL/ygrbuTm7pchAgMBAAECgYEAn8Dp+lEVT88NTwJSA1QREUzZgUph0Ss5TJOLidvGz4saUPre3qQp6gChuNIGwUEjTbwo5fRC1ZXlvKsIZZY/t8c16yolslJ6TdxHVjwI/i4vVpYy/PKwCw2VTpL+3pW/4rv8KPHgiAl4B4+tLJxAIB74TDwuwLNmHD3H9kgLNN0CQQDzHS9n0ZmjszwaGdCPkAvL6G42bMeOBViiwRrMAKFVBDnbYSVIVZCeblYwHW7Bf0BGzn7rlqsz+XrRrmID0mUfkEAxUvM+orA+x2vTLhUy0pzk4B/Xzsrpl4GjyzCzVrVpYGlWEkOetQFGwNOYOYt4njuThPNsnoxFDJNCbASvHk7vwJBAIiJwKEXJ6m3tS6XhvnKFcX8kUGB0IWj3QbzWyBtzi4YRIJAShcY7zL7lu5I6XZFCI171e5sXVTAbckrniK1XFMCQQCeqPGDPdgpWVriyI2wGgRNxxUnIS9eD9kYhHd3qyeKfHLaR430atJcQdFjDVgy+usxMK3HbIpRYo4fT1AR7zCDAkAGdSuElZW+RVR82U+ulz9f1yfl0DrYWsFeWQ4P5RO8x8Dtl+FMv/GTpJlRawNdgGq1BYcJgWJjHNdYh19UFQNz
-----end----
```

-  There was some error in key
-  `https://www.samltool.com/format_privatekey.php` repairs the key

- Final private key

```bash
╰─$ cat private.key

-----BEGIN RSA PRIVATE KEY-----
MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgE
AAoGBALtdcbD3walQVFxgTd8uAxgVarRPtgTHTI7CDnAHVUvvYzDRyZcE31vagVG
3StncJiqc8Nv2yTYRTh5qFLg3192BL3W5vo6Qc7DqHQxja+/21sAnbpQng7zc9yv
H4fh6LLQA/rDS14hrk01PJH96S+cghlbYXPqL/ygrbuTm7pchAgMBAAECgYEAn8D
p+lEVT88NTwJSA1QREUzZgUph0Ss5TJOLidvGz4saUPre3qQp6gChuNIGwUEjTbw
o5fRC1ZXlvKsIZZY/t8c16yolslJ6TdxHVjwI/i4vVpYy/PKwCw2VTpL+3pW/4rv
8KPHgiAl4B4+tLJxAIB74TDwuwLNmHD3H9kgLNN0CQQDzHS9n0ZmjszwaGdCPkAv
L6G42bMeOBViiwRrMAKFVBDnbYSVIVZCeblYwHW7Bf0BGzn7rlqsz+XrRrmID0mU
fAkEAxUvM+orA+x2vTLhUy0pzk4B/Xzsrpl4GjyzCzVrVpYGlWEkOetQFGwNOYOY
t4njuThPNsnoxFDJNCbASvHk7vwJBAIiJwKEXJ6m3tS6XhvnKFcX8kUGB0IWj3Qb
zWyBtzi4YRIJAShcY7zL7lu5I6XZFCI171e5sXVTAbckrniK1XFMCQQCeqPGDPdg
pWVriyI2wGgRNxxUnIS9eD9kYhHd3qyeKfHLaR430atJcQdFjDVgy+usxMK3HbIp
RYo4fT1AR7zCDAkAGdSuElZW+RVR82U+ulz9f1yfl0DrYWsFeWQ4P5RO8x8Dtl+F
Mv/GTpJlRawNdgGq1BYcJgWJjHNdYh19UFQNz
-----END RSA PRIVATE KEY-----
```

### Solve

- Used openssl to solve the RSA

```bash
└─$ openssl rsautl -decrypt -inkey private.key -in ciphertxt.enc
b1NwA1K_15_u5eFu1

```

- Flag

```bash
# Flag : TECHNO(b1NwA1K_15_u5eFu1)

```

