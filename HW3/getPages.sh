#! /bin/bash 

rm -rf pages/
mkdir pages/

while read -r line 
do
	line=$line
	hash=$(echo $line | md5sum | awk '{print $1}')
	curl -X GET $line > ./pages/$hash 

done < ./data/temp
