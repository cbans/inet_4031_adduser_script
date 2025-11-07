#!/usr/bin/python3

# Prompt the user to select dry-run or normal mode.
# In dry-run, no system commands are executed; we just print what would happen.
# In normal mode, os.system() actually runs the commands to add users and set passwords.
# The dry_run variable is used as a flag to check whether to execute commands
# or just simulate them.
import os
import re
import sys

def main():

    # Ask if user wants a dry-run
    choice = input("Dry-run? (Y to simulate, N to run normally): ").strip().upper()
    dry_run = (choice == "Y")

    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(':')

        # If comment line or not enough fields
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("[DRY-RUN] Skipping commented line.")
                elif len(fields) != 5:
                    print("[DRY-RUN] ERROR: Line does not contain 5 fields →", line.strip())
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run:
            print(f"[DRY-RUN] Would run: {cmd}")
        else:
            os.system(cmd)

        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_run:
            print(f"[DRY-RUN] Would run: {cmd}")
        else:
            os.system(cmd)

        for group in groups:
            if group != "-":
                print(f"==> Assigning {username} to group {group}...")
                cmd = f"/usr/sbin/adduser {username} {group}"

                if dry_run:
                    print(f"[DRY-RUN] Would run: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
