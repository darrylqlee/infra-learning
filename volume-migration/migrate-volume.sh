#!/bin/bash


stackname=stack-dev-monitoring_
targethost=docker04
# Extracts volume names which match stackname
volumes=`docker volume ls | grep $stackname | awk '{print $2}'`

#If the return is empty, exit
if [ "x$volumes" = "x" ]; then
    echo "* No volumes found!"
    exit
fi

# For all the volumes returned, perform migration
for volume in $volumes
do
    echo "* Copy Volume $volume to $targethost"
    # Enter the target docker host and recreate an identically named volume
    ssh -q $targethost "docker volume create $volume"

    # Copy command (tar and untar file)
    docker run --rm -v $volume:/from nfdocker01-dev.in.telstra.com.au:8443/devtest/alpine ash -c "cd /from ; tar -cf - . " | ssh -q $targethost "docker run --rm -i -v $volume:/to nfdocker01-dev.in.telstra.com.au:8443/devtest/alpine ash -c \"cd /to ; tar -xpvf - \" "
done
