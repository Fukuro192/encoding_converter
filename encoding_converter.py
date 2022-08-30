#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('string',\
	help='the value to be converted, for example: У·Ц{МъЙ╣Р║СfН▐ПW ')
parser.add_argument('-s', '--source', '--from', required=True,\
	help='the source encoding of the wanted string, for example: IBM866')
parser.add_argument('-d', '--destination', '--to', required=False,\
	help='the destination encoding of the wanted string, for example: Shift_JIS')

args = parser.parse_args()

result = args.string.encode(args.source).decode(args.destination, errors='ignore')

print(result)