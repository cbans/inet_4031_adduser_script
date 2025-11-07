# INET4031 Add Users Script and User List

Program Description

create-users.py automates the creation of Linux user accounts and group memberships. 
Instead of manually running commands like adduser and passwd for each new user, 
this script reads a list of accounts from an input file and generates the required system commands automatically. 
This helps reduce repetitive work, prevents typing errors, and scales easily for bulk user provisioning.

How to Use the Program

## INET4031 Add Users Script and User List

## Program Description

Create-users.py automates the creation of Linux user accounts and group memberships.
Instead of manually running commands like adduser and passwd for each new user,
this script reads a list of accounts from an input file and generates the required system commands automatically.
This helps reduce repetitive work, prevents typing errors, and scales easily for bulk user provisioning.

## How to Use the Program


The script reads user account information from an input file and applies those settings to the system. Because it modifies system users and groups, it must be run with elevated (root) privileges.
Input File Format (create-users.input)
Each line in the file represents one user and must follow this colon-separated format:

username – The Linux login name (ex: user04)
password – The account’s initial password
last_name/ first_name – Used to fill in the system’s user description field (GECOS)
groups – A comma-separated list of supplemental groups (ex: group01,group02)
Use - if the user should not be added to any extra groups


Skipping Lines:
To skip a line (for notes or temporary removal), start the line with #.

Command Execution

## Skipping Lines:
To skip a line (for notes or temporary removal), start the line with #.

## Command Execution


The script must have executable permission set (e.g., $ chmod +x create-users.py) and is run from the command line using input redirection with elevated privileges.
The necessary execution command is: sudo ./create-users.py < create-users.input


Dry Run

A Dry Run is a crucial safety feature that allows the user to test the script's logic and ensure it generates the 

## Dry Run

A Dry Run is a crucial safety feature that allows the user to test the script's logic and ensure it generates the
correct commands without making any permanent modifications to the system. To enable a dry run, the user must:

Comment out the three lines containing os.system(cmd).

Uncomment the three lines containing print(cmd).

When run in this mode, the script will execute all its internal logic but will only output the exact adduser and passwd commands 
When run in this mode, the script will execute all its internal logic but will only output the exact adduser and passwd commands
that would have been run, allowing the user to check for errors before committing the changes.
