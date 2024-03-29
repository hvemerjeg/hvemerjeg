#THIS CODE IS FOR VALIDATING IPv4 ADDRESSES AND IPv6 ADDRESSES
import re #We are going to need the module to perform regular expressions
import os  

def validatingIP(ip_address: str):
	IPv4_PATTERN = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
	IPv6_PATTERN = '^([0-9a-f]{0,4}:){7}[0-9a-f]{0,4}$'
	
	if re.search(IPv4_PATTERN, ip_address):
		return f"\033[1;32;40m{ip_address} --> IPv4\033[0m"
	elif re.search(IPv6_PATTERN, ip_address):
		return f"\033[1;33;40m{ip_address} --> IPv6\033[0m"
	return f"\033[1;31;40m{ip_address} --> Not an IP address\033[0m"


if __name__ == '__main__':
	#TESTS
	#In this case I was using a file named ip_address.txt with a bunch of valid and invalid IP addresses to do some tests.
	try:
		file = open("ip_address.txt", "rt")
		for line in file:
			print(validatingIP(line.strip()))
	except IOError as e:
		print("\033[1;31;40mI/O Error occured: {os.strerror(e.errno)}\033[0m")
