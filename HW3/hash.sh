#! /bin/bash

rm LUT
while read -r line
do 
	line=$line
	hash=$(echo $line | md5sum | awk '{print $1 }')
	echo $hash, $line >> LUT
done < ./data/temp
