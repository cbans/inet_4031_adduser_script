#!/usr/bin/python3

# INET4031
# Carter Chen
# 11/6/2025
# 11/7/2025

# Import necessary modules for OS interaction, Regular Expressions, and Standard Input.
import os
import re
import sys



def main():
    for line in sys.stdin:

        #Iterate through each line read from Standard Input (stdin), which is piped
        #from the create-users.input file via the '<' redirection operator.
        match = re.match("^#",line) # This character is used as a skip mechanism to ignore commented lines in the input file.

        # Remove leading/trailing whitespace and split the line into a list of fields
        fields = line.strip().split(':')

        #This conditional statement checks for two exclusion conditions
        #If 'match' is true (the line is commented out).
        #If the line does not contain exactly 5 data fields.
        #If either condition is true, the 'continue' keyword skips the rest of the loop
        #and moves to the next line of input, preventing runtime errors.
        if match or len(fields) != 5:
            continue

        #Map the colon-delimited fields from the input file to clear variable names.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This line splits that field into a list of individual group names.
        groups = fields[4].split(',')

        #Print a status message to the console indicating the start of the account creation process
        print("==> Creating account for %s..." % (username))
        #Execute the generated Linux command to create the user account on the system.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Currently set for Dry Run: Prints the command

        #print (cmd)
	#Uncomment this line and comment the 'print' line for Live Run
        os.system(cmd)

        #Print a status message to the console indicating the start of the password setting process.
        print("==> Setting the password for %s..." % (username))
        #This command uses 'echo' to pipe the password (twice) into 'passwd' via 'sudo' to set the password without user interaction.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Execute the generated Linux command to set the user's password.
        # Currently set for Dry Run: Prints the command
        #print (cmd)
	# Uncomment this line and comment the 'print' line for Live Run
        os.system(cmd)

        for group in groups:
            #Check if the group name is NOT a hyphen ('-'). The hyphen is used in the input file
	    #to signify that the user should not be added to any supplemental groups.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print (cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
