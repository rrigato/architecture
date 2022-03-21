#!/bin/bash
################################
#parses a csv config file to create an alias for 
#each command
#
################################
INPUT=alias_commands.csv
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read alias_name alias_value
do
	alias $alias_name="$alias_value"
done < $INPUT
IFS=$OLDIFS