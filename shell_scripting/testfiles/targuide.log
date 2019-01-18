##### COMPRESSION:
tar -cvf test1.tar testfiles/
Creates tar archive.  
c - creates new .tar archive file
v - verbosely show .tar file progress (optional)
f - file name type of archive file

tar cvfz test2.tar.gz testfiles/
tar cvfz test2.tgz testfiles/
Creates tar.gz archive, more compressed.
z - gzip compression

tar cvfj test3.tar.bz2 testfiles/
tar cvfj test3.tar.tbz testfiles/
tar cvfj test3.tar.tb2 testfiles/
Higher compression than gz
j - highly compressed tar file.

tar -rvf test1.tar ex1.sh
tar -rvf test1.tar testfiles
Append files / folder to tar file.  
Cannot be used with compressed archives.

##### DECOMPRESSION:
tar -xvf test1.tar [-C /directory/]
tar -xvf test2.tar.gz  [-C /directory/]
tar -xvf test3.tar.bz2
Extract files from any tar

tar -xvf test1.tar ex1.sh
tar -zxvf test2.tar ex2.sh
tar -jxvf test3.tar ex3.sh
Extract single file from tar archive

tar --extract --file=test1.tar ex1.sh
Universal extractor

tar -xvf/-zxvf/-jxvf "file1" "file2"
Extract multiple files by name

tar -xvf/-zxvf/-jxvf --wildcards '*.jpg'
Extract using wildcard

##### SHOW CONTENTS:
tar -tvf test1.tar
