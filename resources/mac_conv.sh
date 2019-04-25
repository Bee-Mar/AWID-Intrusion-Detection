#!/bin/bash

# to view formatting of MAC address list
macchanger --list | head

# trim the first column indicating the row number, and replace " - " to a tab for CSV formatting
macchanger --list | cut -c 8- > mac_addresses && sed -i 's/ - /\t/g' mac_addresses

# remove all leading whitespace and rename the file to mac_addr.tsv
sed -i 's/^[ \t]*//;s/[ \t]*$//' mac_addresses && mv mac_addresses mac_addr.tsv

# view the formatting
head mac_addr.tsv

# find out which lines have multiple dashes
egrep -o "^[-]*" -nr mac_addr.tsv

# delete those line numbers
sed -i -e '3d;19018d' mac_addr.tsv

# view top and bottom of the csv
head mac_addr.tsv
tail -50 mac_addr.tsv

# from here, the rest was done manually
