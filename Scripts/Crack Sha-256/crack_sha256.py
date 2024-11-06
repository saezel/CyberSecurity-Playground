"""
Generate test hash : echo -ne python | sha256sum

Run: python3 crack_sha256.py <hash>

"""
 

from pwn import *
import sys


if len(sys.argv) != 2:
	print("Invalid arguments")
	print(f">> {sys.argv[0]} <sha256sum>")
	exit()


wanted_hash = sys.argv[1]
password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0

with log.progress(f"Attempting to crack {wanted_hash} \n") as p:
	with open(password_file, "r", encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sumhex(password)

			p.status(f"[{attempts}] {password.decode('latin-1')} == {password_hash} \r")
			if password_hash == wanted_hash:
				p.success(f"Hash found: [{(password.decode('latin-1'))}]  == {password_hash}")
				exit()

			attempts += 1
		p.failure("Password hash not found")