# Giftwrap [ Reversing ]

![image](https://user-images.githubusercontent.com/56447720/149666955-e183ad60-55d9-44cc-a23a-c9c115ee7a6b.png)

#### This is day 2 challenge

## Binary Info 

```bash
└─$ strings giftwrap 
<--SNIPPED-->
A	?un
G7FA	te
who1D
=ddr
}643e
Pb+4%
to]"
-id%ABI-0
2.OZo
AIX5
ot	+
.bss
!$_\
K[lbO
16 8
,6H_
^lOW
s:m/
UPX!
UPX!
             
```

- by using strings we get to know the binary is compressed by UPX
- What is UPX ?
> UPX achieves an excellent compression ratio and offers very fast decompression. Your executables suffer no memory overhead or other drawbacks for most of the formats supported, because of in-place decompression

### Decompressing the binary

```bash
└─$ upx -d giftwrap            
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    925312 <-    357628   38.65%   linux/amd64   giftwrap

Unpacked 1 file.

```

## Analyzing Binary

```bash
└─$ ./giftwrap 
What's the magic word? asdf
Wrong password! Who are you?!?
                                    
```     
- The binary is a typical crackme challenge

- Let's boot up the binary in ghidra

### Main function

- Each character of the user input is `xored` with `0xf3`

```c
<--SNIPPED-->
printf("What\'s the magic word? ");
  __isoc99_scanf("%256s",&user_input);
  local_11c = 0;
  while (local_11c < 0x100) {
    *(byte *)((long)&user_input + (long)(int)local_11c) =
         *(byte *)((long)&user_input + (long)(int)local_11c) ^ 0xf3;
    local_11c = local_11c + 1;
  }
  iVar1 = thunk_FUN_004010e6(CHECK,&user_input,0x17);
  if (iVar1 == 0) {
    puts("Welcome inside...");
  }
  else {
    puts("Wrong password! Who are you?!?");
  }
```

- After xoring the value ( xored input ) is compared with `CHECK` variable 

## Solution

- Let's the data stored in `CHECK` variable 

```asm
                             CHECK                                           XREF[3]:     Entry Point(*), main:004019fa(*), 
                                                                                          main:00401a01(*)  
        004cc0f0 bb a7 b1        undefine
                 88 86 83 
                 8b ac c7 
           004cc0f0 bb              undefined1BBh                     [0]                               XREF[3]:     Entry Point(*), main:004019fa(*), 
                                                                                                                     main:00401a01(*)  
           004cc0f1 a7              undefined1A7h                     [1]
           004cc0f2 b1              undefined1B1h                     [2]
           004cc0f3 88              undefined188h                     [3]
           004cc0f4 86              undefined186h                     [4]
           004cc0f5 83              undefined183h                     [5]
           004cc0f6 8b              undefined18Bh                     [6]
           004cc0f7 ac              undefined1ACh                     [7]
           004cc0f8 c7              undefined1C7h                     [8]
           004cc0f9 c2              undefined1C2h                     [9]
           004cc0fa 9d              undefined19Dh                     [10]
           004cc0fb 87              undefined187h                     [11]
           004cc0fc ac              undefined1ACh                     [12]
           004cc0fd c6              undefined1C6h                     [13]
           004cc0fe c3              undefined1C3h                     [14]
           004cc0ff ac              undefined1ACh                     [15]
           004cc100 9b              undefined19Bh                     [16]
           004cc101 c7              undefined1C7h                     [17]
           004cc102 81              undefined181h                     [18]
           004cc103 97              undefined197h                     [19]
           004cc104 d2              undefined1D2h                     [20]
           004cc105 d2              undefined1D2h                     [21]
           004cc106 8e              undefined18Eh                     [22]
           004cc107 00              undefined100h                     [23]
```

- Let's store the `CHECK` values locally and `xor` it with `0xf3` to get flag

## solve.py

```py

check_values = 'bb a7 b1 88 86 83 8b ac c7 c2 9d 87 ac c6 c3 ac 9b c7 81 97 d2 d2 8e 00'.split(' ')
int_values = [int(i,16) for i in check_values]

flag = ''.join([chr(i ^ 0xf3) for i in int_values])
print(flag)
```

## Flag 

```bash
└─$ ./giftwrap 

What's the magic word? 
HTB{upx_41nt_50_h4rd!!}ó
Welcome inside...

# flag : HTB{upx_41nt_50_h4rd!!}ó

```











