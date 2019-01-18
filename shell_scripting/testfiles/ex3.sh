#!/bin/bash

#Ex1
echo "This script will exit with a 0 exit status."
exit 0

#Ex2
# Taking first script argument
ex2arg="$1"
if [ -f $ex2arg ]
then
    exit 0
elif [ -d $ex2arg ]
then
    exit 1
else
    exit 2
fi

#Ex3
cat /etc/shadow
if [ "$?" -eq 0 ]
then
    echo "Command Succeeded"
    exit 0
else
    echo "Command Failed"
    exit 1
fi
