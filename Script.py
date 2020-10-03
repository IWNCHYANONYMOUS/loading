import sys
import time

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + '[*] Loading... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()
