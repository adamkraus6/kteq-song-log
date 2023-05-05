#!/usr/bin/python3

import json

class PSA(object):
		def __init__(self):
			self.list = []

			with open('psa.json') as data_file:
				p = json.load(data_file)
				for psa in p['PSAs']:
						self.list.append(psa['title'])

if __name__ == '__main__':
	print("Current PSAs in Rotation: ")
	p = PSA()
	for psa in p.list:
		print(psa)
