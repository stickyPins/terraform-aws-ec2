#!/bin/bash

# This script displays information about the system on which it is executed

# Tell the user the script is starting
echo "The script is starting"

# Display the hostname of the system
hostname

# Display the date and time when this information was collected
date

# Display the kernel release followed by architecture

# This is the kernel release
uname -r

uname -m
This displays the architecture or the hardware

# Display disk usage in human readable format
df -h
# End the script by letting user know it is done

# Display the current month calendar 
cal

echo "The script has ended"