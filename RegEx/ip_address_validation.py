import re
import os

def validatingIP(ip_address: str):
	IPv4_PATTERN = '^(([0-9]|[1-9][0-9]|[1-2][0-9][0-9])\.){3}([0-9]|[1-9][0-9]|[1-2][0-9][0-9])$'
	IPv6_PATTERN = '^([0-9a-f]{0,4}:){7}[0-9a-f]{0,4}$'
	
	if re.search(IPv4_PATTERN, ip_address):
		return "\033[1;32;40mIPv4\033[0m"
	elif re.search(IPv6_PATTERN, ip_address):
		return "\033[1;33;40mIPv6\033[0m"
	return "\033[1;31;40mNot an IP address\033[0m"


if __name__ == '__main__':
	#TESTS
	#In this case we are using a file named ip_address.txt with a bunch of valid and invalid IP addresses to do some tests
	try:
		file = open("ip_address.txt", "rt")
		for line in file:
			print(validatingIP(line))
	except IOError as e:
		print("\033[1;31;40mI/O Error occured: {os.strerror(e.errno)}\033[0m")	
