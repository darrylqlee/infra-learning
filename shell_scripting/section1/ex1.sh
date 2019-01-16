#!/bin/bash

# Ex1 / Ex2
# Simple echo
WORDS="Shell Scripting is aight..."
echo ${WORDS}

# Ex3
# Echo function call
host_name=$(hostname)
echo "This script is running on ${host_name}."

# Ex4: Check file permissions on file

for infiles in $@
do
    if [ -e $infiles ]
    then
        echo "${infiles} found."
        if [ -w "${infiles}" ]
        then
            echo "You have permissions to edit ${infiles}."
        else
            echo "You do NOT have permissions to edit ${infiles}."
        fi
    else
        echo "${infiles} cannot be found."
    fi
done

# Ex5
animals="man bear pig dog cat"
echo $animals

for animal in $animals
do
    echo $animal
done

# Ex6
read -p "Give me a file: " varfile
if [ -f $varfile ]
then
    echo "${varfile} is a file."
elif [ -d $varfile ]
then
    echo "${varfile} is a directory."
else   
    echo "You have some other type of file, or I didn't find it."
fi
Echo "Directory listing:"
echo $(ls -lart ${varfile})

# Skip Ex7 - see Ex6

# Ex8 - see Ex4

