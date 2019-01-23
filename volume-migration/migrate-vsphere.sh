#!/bin/bash

# This script needs to be run from the volume is stored locally.
read -p "Stack name: " stackmatch  #darryl-test_testvol
targethost=docker01
storage="@hxdockerds01"
discsize="5GB"

# Extracts volume names which match stackname
vvolumes=`docker volume ls | grep ${stackmatch} | awk '/vsphere/ {print $2}'`
lvolumes=`docker volume ls | grep ${stackmatch} | awk '/local/ {print $2}'`

echo "Existing vsphere volumes:
${vvolumes}"

#If the return is empty, exit
if [ "x${lvolumes}" = "x" ]; then
    echo "* No local volumes found!"
    # exit
fi
echo "Found local volumes:
${lvolumes}"

# For all the volumes returned, perform migration
for volume in $lvolumes
do
    echo "* Copy Volume ${volume} to vSphere volume..."
    # Enter the target docker host and create an equivalent vSphere volume
    ssh -q ${targethost} "docker volume create --driver=vsphere:latest --name=${volume} -o size=${discsize}"

    # Copy command (tar and untar file).  This is carried out on the local docker host
    if [ $? = 0 ]; then
        docker run --rm -v ${volume}:/from nfdocker01-dev.in.telstra.com.au:8443/devtest/alpine ash -c "cd /from ; tar -cf - . " | docker run --rm -i --volume-driver vsphere -v ${volume}${storage}:/to nfdocker01-dev.in.telstra.com.au:8443/devtest/alpine ash -c "cd /to ; tar -xpvf - "
    else   
        echo "Volume copying failed..."
    fi
done

echo "Migration complete."


# # Remove containers completely from target host before continuing
# docker ps -a | grep ${stackmatch} | awk '{print $1}' > isempty
# echo ${isempty}
# if [ "x${isempty}" = "x" ]; then
#     echo "Containers already removed. Continuing with migration..."
# else    
#     for containers in $isempty
#     do
#         docker rm ${containers}
#         echo "Container removed."
#     done
# fi 
    