#!/usr/bin/env python3
import sys

def print_help():
    tool_name = "Combine Lists Tool"
    box_width = len(tool_name) + 4

    print(f"\033[1;33m{'*' * box_width}")
    print(f"* \033[1;32m{tool_name.upper()}\033[1;33m *")
    print(f"{'*' * box_width}\033[0m")

    print("\n\033[1;36mDESCRIPTION:")
    print("  Combine user and password lists into a single file.")

    print("\n\033;USAGE:")
    print(f"  python {sys.argv[0]} -users <userlist.txt> -pass <passlist.txt>\033[0m")

    print("\n\033[1;93mOPTIONS:")
    print("  -users <userlist.txt>: Path to userlist file")
    print("  -pass <passlist.txt>: Path to passlist file")
    print("  -h: Help\033[0m")

def combine_lists(user_file, pass_file, output_file):
    with open(user_file, 'r') as users, open(pass_file, 'r') as passwords, open(output_file,'w') as output:
        for user, password in zip(users, passwords):
            user = user.strip()
            password = password.strip()
            combined_line = f"{user}:{password}\n"
            output.write(combined_line)

            if not user or not password:
                 print("\033[1;32mCombination completed. Terminating...\033[0m")
                 break

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        sys.exit(0)
    if len(sys.argv) != 5 or sys.argv[1] != '-users' or sys.argv[3] != '-pass':
        print("Usage: combine.py -users <userlist.txt> -pass <passlist.txt>")
        sys.exit(1)

    user_file = sys.argv[2]
    pass_file = sys.argv[4]
    output_file = 'wordlist.txt'

    combine_lists(user_file, pass_file, output_file)

if __name__ == "__main__":
    main() 
