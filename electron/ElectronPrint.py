# -*- coding: utf-8 -*-
import sys
# This script print out the electron configurations of elements
# The user provide the total number of electron and the script 
# print out the electron configuration of the element

shells = {'s':2, 'p':6, 'd':5, 'f':7}
orbitals = [
			'1s', 
			'2s','2p',  
			'3s','3p','4s', 
			'3d','4p','5s','4d', 
			'5p','6s','4f','5d', 
			'6p','7s','5f','6d', 
			'7p','8s','6f','7d', 
			'8p','9s','7f','8d', 
			'9p','10s','8f','9d',
			'10p','11s','9f','10d', 
			'11p','12s','10f', 
			'11d','12p', 
			'13s']

n = int(sys.argv[1])

for i in orbitals:
	if n<=0:
		break
	for j in shells.keys():
		if j in shells.keys():
			if j in i:
				m = n
				n = n - shells[j]
				if n < 0:
					print(i,m)
					break
				else:
					print(i,shells[j])