#!/bin/bash

## USAGE:
# Parameter 1 - full working directory
# Parameter 2 - desired rename date

echo "Executing script: $0"
#sleep 3
FRUIT="apple"

## IF STATEMENTS
if [ "${FRUIT}" = "apple" ]
then
    echo "yeahboi"
elif [ "${FRUIT}" = "banana" ]
then
    echo "banyanya"
else
    echo "boi..."
fi

# CHARACTER ARRAYS / DO STATEMENT
COLORS="red green blue"
for COLOR in $COLORS
do
    echo "COLOR: $COLOR"
done

# OBTAIN RESULTS FROM COMMAND LINE
echo $1
WORKING_DIR=$1
echo $WORKING_DIR
PICS=$(cd ${WORKING_DIR}; ls *jpg)     # obtain filenames only
DATE=$2
#DATE=$(date +%F)    # Today's date

for PICTURE in $PICS
do
    echo "Renaming ${PICTURE} to ${DATE}-${PICTURE}"
    mv ${WORKING_DIR}/${PICTURE} ${WORKING_DIR}/${DATE}-${PICTURE}
done
