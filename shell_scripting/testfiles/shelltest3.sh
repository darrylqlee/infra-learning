#!/bin/bash
# 0 exit code is success.  Otherwise is error (1-255)

# Echo return code of previous command
ls /not/here
echo "$?"

ls testfiles
echo "$?"

HOST="www.google.com"
ping $HOST
if [ "$?" -eq "0" ]
then
    echo "$HOST reachable."
fi

# If first command succeeds, run second.
mkdir /test && cp testfiles /test
# If first command fails, run second.
cp abc /test || mkdir /test

# The above statement can be converted to:
ping $HOST || echo "$HOST unreachable."

# Specify return code of script/stop execution. By default last command executed.
exit 0   
