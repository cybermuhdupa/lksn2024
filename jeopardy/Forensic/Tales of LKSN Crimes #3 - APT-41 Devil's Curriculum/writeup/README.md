```
1. The attacker seems to build a custom rootkit-like kernel object to the victim OS. What's the kernel module load address for that rootkit?

Answer is in the hexadecimal address form 

For example if it's in the 0xffffffffabcdc0fe then the answer is 0xffffffffabcdc0fe

Answer >> 0xffffffffc0551000

2. There's a zip file that is created by the user. This file is password-protected and it is cached. In what inode number that this file is cached?

Answer format is in integer.

Example, if it is resided in inode number 765 then the answer is 765.

Answer >> 2095015

3. It seems the password that is used for the zip file is stored in a linux variable. Can you find its variable name? And what is the value of that? This will indicate its password

Answer format is NAMEOFTHEVARIABLE_VALUE

For example, you found that the password is stored in Linux variable called jaBa, and the value of jaja is pass123. So the answer is jaBa_pass123

Answer >> FANATIC_cZn5xU67st3LI

4. The uncovered zip content may leaks the APT plan in order to breach their targeted victim company and usually it involves a name of their higher ups. 
Can you tell us WHO will likely to be targeted (not an OSINT challenge) ?

Answer is the name format. 
Example if the name is Robi Jamada then please input it with space replaced by underscore -> Robi_Jamada

Answer >> Armin_Bahanang
```







