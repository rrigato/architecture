#!/bin/bash
################################
#parses a csv config file to create an alias for 
#each command
#use alias command to list all alias that are present
################################

while IFS=',' read alias_name alias_value
do
    alias $alias_name="$alias_value"
done < <(tail -n +2 ~/shell_config/alias_commands.csv)